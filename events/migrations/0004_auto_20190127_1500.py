# Generated by Django 2.1.4 on 2019-01-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190120_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='gallerie',
            field=models.FilePathField(allow_folders=True, blank=True, null=True, path='/static/'),
        ),
    ]
