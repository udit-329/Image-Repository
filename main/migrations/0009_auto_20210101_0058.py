# Generated by Django 3.1.4 on 2020-12-31 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210101_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(null=True, upload_to='image_folder', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
