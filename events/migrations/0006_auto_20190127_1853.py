# Generated by Django 2.1.4 on 2019-01-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190127_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='gallerie',
            field=models.FilePathField(allow_folders=True, blank=True, null=True),
        ),
    ]
