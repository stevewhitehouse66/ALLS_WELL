# Generated by Django 4.2.1 on 2024-03-07 13:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_delete_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
