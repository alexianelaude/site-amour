# Generated by Django 2.1.4 on 2019-03-30 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190330_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 30, 15, 37, 20, 699503, tzinfo=utc), verbose_name='date published'),
        ),
    ]