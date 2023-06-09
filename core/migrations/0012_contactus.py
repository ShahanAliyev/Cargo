# Generated by Django 3.2 on 2023-03-27 09:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20230327_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^\\d{7}$', message='Please enter valid phone number')])),
                ('working_hours', models.CharField(max_length=16)),
                ('phone_prefix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.phoneprefix')),
            ],
            options={
                'verbose_name': 'Contact US',
                'verbose_name_plural': 'Contact US',
            },
        ),
    ]
