# Generated by Django 3.2 on 2023-04-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_localwarehouse'),
        ('user', '0017_alter_user_warehouse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WareHouse',
        ),
    ]
