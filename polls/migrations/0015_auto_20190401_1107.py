# Generated by Django 2.1.4 on 2019-04-01 09:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20190401_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 1, 9, 7, 53, 408516, tzinfo=utc), verbose_name='date published'),
        ),
    ]
