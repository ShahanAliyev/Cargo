# Generated by Django 3.2 on 2023-05-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_merge_20230502_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foreignwarehouse',
            name='flexible_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foreignwarehouse',
            name='name_surname',
            field=models.CharField(default="[User's name and surname]", max_length=64),
        ),
    ]
