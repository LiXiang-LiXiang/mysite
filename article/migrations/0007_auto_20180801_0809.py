# Generated by Django 2.0.6 on 2018-08-01 00:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180730_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 9, 48, 160833, tzinfo=utc)),
        ),
    ]
