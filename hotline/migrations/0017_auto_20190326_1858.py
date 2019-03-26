# Generated by Django 2.1.4 on 2019-03-26 17:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0016_auto_20190325_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apero',
            name='avec_alcool',
        ),
        migrations.AddField(
            model_name='apero',
            name='biere',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apero',
            name='cidre',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apero',
            name='cocktail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apero',
            name='vege',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apero',
            name='vin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apero',
            name='virgin_cocktail',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='apero',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 26, 17, 58, 49, 934116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='crepes',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 26, 17, 58, 49, 934116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='muffin',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 26, 17, 58, 49, 934116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='petitdej',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 26, 17, 58, 49, 934116, tzinfo=utc)),
        ),
    ]
