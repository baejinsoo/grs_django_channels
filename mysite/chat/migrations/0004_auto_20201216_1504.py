# Generated by Django 3.1.4 on 2020-12-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20201216_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/imgaes/'),
        ),
    ]
