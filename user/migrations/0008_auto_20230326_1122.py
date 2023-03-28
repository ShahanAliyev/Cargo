# Generated by Django 3.2 on 2023-03-26 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20230326_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gov_id',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator('^\\d{7}$', message='Please enter your valid phone number')]),
        ),
    ]