# Generated by Django 2.1.4 on 2019-04-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0003_auto_20190329_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesure',
            name='concret',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mesure',
            name='constat',
            field=models.TextField(blank=True, null=True),
        ),
    ]