# Generated by Django 3.1.4 on 2021-01-01 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210101_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(null=True, upload_to='image_folder', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'jpe', 'jif', 'png', 'gif', 'webp', 'tiff', 'tif'], 'File type not supported')]),
        ),
    ]
