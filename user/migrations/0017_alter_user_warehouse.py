# Generated by Django 3.2 on 2023-04-18 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_localwarehouse'),
        ('user', '0016_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.localwarehouse'),
        ),
    ]
