# Generated by Django 2.1.7 on 2019-03-22 23:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190323_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowitem',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 0, 20, 32, 453054)),
        ),
    ]
