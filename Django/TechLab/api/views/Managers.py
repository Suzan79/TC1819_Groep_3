from django.conf import settings
from django.http.response import JsonResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
import datetime

from api.models import (User)
from django.contrib.auth.models import User as AuthUser
import json


class Managers(View):
    def get(self, request, *args, **kwargs):
        managers = User.objects.filter(is_manager=True)

        return JsonResponse(json.loads(json.dumps([manager.to_json('_state') for manager in managers])), safe=False, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if not (i in request.POST for i in ['email']):
            return JsonResponse(json.loads('{"success": "false", "message": "Missing argument email. "}'),
                                safe=False, status=400)

        manager, created = User.objects.get_or_create(
            email=request.POST.get('email'),
            defaults={'is_manager': True},
        )

        if not created:
            manager.is_manager = True
            manager.save()

        return JsonResponse(json.loads('{"success": "true", "message": "The user has been added as Manager. "}'),
                            safe=False, content_type='application/json')

class Manager(View):
    def get(self, request, pk, *args, **kwargs):
        admin = AuthUser.objects.filter(id=pk)
        if admin.count() > 0:
            json_dict = vars(admin.first())
            print(json_dict)
            json_dict.pop('_state', None)
            json_dict.pop('password', None)
            json_dict.pop('last_login', None)
            json_dict.pop('date_joined', None)
            return JsonResponse(json.loads(json.dumps(json_dict)), safe=False)
        manager = get_object_or_404(User, id=pk, is_manager=True)

        return JsonResponse(json.loads(json.dumps(manager.to_json('_state'))), safe=False, content_type='application/json')

    def put(self, request, pk, *args, **kwargs):
        manager = get_object_or_404(User, id=pk)

        manager.is_manager = True
        manager.save()

        return JsonResponse(json.loads('{"success": "true", "message": "The user has been added as Manager. "}'), safe=False, content_type='application/json')

    def delete(self, request, pk, *args, **kwargs):
        manager = get_object_or_404(User, id=pk)

        manager.is_manager = False
        manager.save()

        return JsonResponse(json.loads('{"success": "true", "message": "The user has been removed as Manager. "}'), safe=False, content_type='application/json')
