# Generated by Django 3.1.4 on 2020-12-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201224_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_date',
        ),
        migrations.AddField(
            model_name='image',
            name='image_picture',
            field=models.ImageField(null=True, upload_to='image_folder'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(default='new_image', max_length=200),
        ),
    ]
