# Generated by Django 2.1.7 on 2019-03-24 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190324_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowitem',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 16, 48, 32, 804456)),
        ),
        migrations.AlterField(
            model_name='borrowitem',
            name='hand_in_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 16, 48, 32, 804456)),
        ),
        migrations.AlterField(
            model_name='borrowitem',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 16, 48, 32, 804456)),
        ),
    ]
