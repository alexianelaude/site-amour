# Generated by Django 2.1.4 on 2019-04-02 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0023_auto_20190401_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apero',
            name='delivery_place',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='crepes',
            name='delivery_place',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='muffin',
            name='delivery_place',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='petitdej',
            name='delivery_place',
            field=models.CharField(max_length=500),
        ),
    ]