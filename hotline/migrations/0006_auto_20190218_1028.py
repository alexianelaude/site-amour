# Generated by Django 2.1.4 on 2019-02-18 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0005_auto_20190218_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crepes',
            name='delivered',
        ),
        migrations.AlterField(
            model_name='crepes',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 18, 9, 28, 8, 30851, tzinfo=utc)),
        ),
    ]
