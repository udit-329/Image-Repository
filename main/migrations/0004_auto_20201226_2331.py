# Generated by Django 3.1.4 on 2020-12-26 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201224_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_picture',
            new_name='picture',
        ),
    ]
