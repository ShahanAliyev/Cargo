# Generated by Django 3.2 on 2023-04-02 11:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20230401_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
