# Generated by Django 2.1.4 on 2019-03-27 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0020_auto_20190327_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apero',
            name='biere',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='apero',
            name='cidre',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='apero',
            name='cocktail',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='apero',
            name='vege',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='apero',
            name='vin',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='apero',
            name='virgin_cocktail',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(1)]),
        ),
    ]