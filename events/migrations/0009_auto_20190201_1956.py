# Generated by Django 2.1.4 on 2019-02-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20190127_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='gallerie',
            field=models.FilePathField(allow_folders=True, blank=True, null=True, path='media/'),
        ),
    ]