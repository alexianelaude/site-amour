# Generated by Django 2.1.4 on 2019-03-31 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190331_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 31, 13, 12, 32, 188775, tzinfo=utc), verbose_name='date published'),
        ),
    ]