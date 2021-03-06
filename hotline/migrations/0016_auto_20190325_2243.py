# Generated by Django 2.1.4 on 2019-03-25 21:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotline', '0015_auto_20190325_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muffin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_time', models.TimeField()),
                ('delivery_date', models.DateField(default=datetime.datetime(2019, 3, 25, 21, 43, 21, 280468, tzinfo=utc))),
                ('delivery_place', models.CharField(max_length=500)),
                ('comment', models.TextField(blank=True, null=True)),
                ('gout_muffin', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='apero',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 25, 21, 43, 21, 280468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='crepes',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 25, 21, 43, 21, 280468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='petitdej',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 25, 21, 43, 21, 280468, tzinfo=utc)),
        ),
    ]
