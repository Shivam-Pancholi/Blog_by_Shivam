# Generated by Django 3.1 on 2020-08-16 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200816_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 15, 14, 33, 332006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 15, 14, 33, 332969, tzinfo=utc)),
        ),
    ]
