# Generated by Django 2.0.6 on 2018-08-01 08:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20180801_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 8, 25, 28, 595398, tzinfo=utc)),
        ),
    ]
