# Generated by Django 2.1.5 on 2019-02-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.TextField(blank=True),
        ),
    ]