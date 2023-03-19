# Generated by Django 3.2 on 2023-03-19 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_fin_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fin_code',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9A-Za-z]{7}$', message='Fin Code has to be 7 characters with letters and digits')]),
        ),
    ]
