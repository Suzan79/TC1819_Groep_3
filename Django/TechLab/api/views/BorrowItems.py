from django.conf import settings
from django.http import QueryDict
from django.http.response import JsonResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
import datetime
from django.apps import apps

from api.models import (BorrowItem, User, Item)

import json


class BorrowItems(View):
    def get(self, request, *atgs, **kwargs):
        email = request.GET.get('email', '*')
        allBorrowedItems = BorrowItem.objects.filter(hand_in_date=None)

        return JsonResponse(json.loads(
            json.dumps([borrowItem.to_json('_state', 'item_ptr_id', 'writers') for borrowItem in allBorrowedItems]),
        ), safe=False)

    def put(self, request, *args, **kwargs):
        put = json.loads(request.body.decode('UTF-8'))
        print(put)

        if not (i in request.POST for i in ['email', 'item_id', 'borrow_date']):
            return JsonResponse(json.loads('{"success": "false", "message": "Missing argument(s). "}'),
                                safe=False, status=400)

        user, created = User.objects.get_or_create(email=put.get('email'), defaults={'email': put.get('email'),
                                                                                     'is_manager': False})
        if created:
            user.save()

        item = get_object_or_404(Item, id=put.get('item_id'))
        model_item = apps.get_model(app_label='api', model_name=item.type).objects.get(id=item.id)

        if model_item.stock > 0:
            borrowItem = BorrowItem.objects.create(user=user, item=item, borrow_date=put.get('borrow_date'))
            borrowItem.save()
            borrowItem.return_date = datetime.datetime.strptime(borrowItem.borrow_date, '%Y-%m-%d %H:%M:%S') + \
                                     datetime.timedelta(days=item.borrow_days)
            borrowItem.save()

            model_item.stock -= 1
            model_item.save()

            return JsonResponse(json.loads('{"success": "true"}'), safe=False)
        return JsonResponse(json.loads('{"success": "false", "message": "No item available"}'), safe=False)


class ReturnItems(View):
    def get(self, request, *atgs, **kwargs):
        email = request.GET.get('email', '*')
        allBorrowedItems = BorrowItem.objects.exclude(hand_in_date=None)

        return JsonResponse(json.loads(
            json.dumps([borrowItem.to_json('_state', 'item_ptr_id', 'writers') for borrowItem in allBorrowedItems]),
        ), safe=False)

    def put(self, request, pk, *args, **kwargs):
        put = json.loads(request.body.decode('UTF-8'))
        print(put)

        borrowItem = get_object_or_404(BorrowItem, id=pk)

        borrowItem.hand_in_date = datetime.datetime.now()
        borrowItem.save()
        try:
            model_item = apps.get_model(app_label='api', model_name=item.type).objects.get(id=borrowItem.item.id)

            if put['broken'] == 'True':
                model_item.broken += 1
            else:
                model_item.stock += 1

            model_item.save()
        except:
            pass

        return JsonResponse(json.loads('{"success": "true"}'), safe=False)

