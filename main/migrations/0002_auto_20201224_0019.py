# Generated by Django 3.1.4 on 2020-12-23 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 24, 0, 19, 8, 698677), verbose_name='date published'),
        ),
    ]
