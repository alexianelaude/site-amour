# Generated by Django 2.1.4 on 2019-03-29 15:17

from django.db import migrations, models
import team.models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listeux',
            name='gif',
            field=models.ImageField(null=True, upload_to=team.models.rename_gif),
        ),
    ]