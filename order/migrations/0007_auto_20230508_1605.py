# Generated by Django 3.2 on 2023-05-08 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20230507_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterModelOptions(
            name='statushistory',
            options={'verbose_name_plural': 'Status Histories'},
        ),
    ]
