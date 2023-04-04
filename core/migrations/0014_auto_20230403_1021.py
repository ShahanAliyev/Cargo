# Generated by Django 3.2 on 2023-04-03 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='discount',
            name='constant_or_percentage',
            field=models.CharField(choices=[('constant', 'Constant'), ('percentage', 'Percentage')], default='percentage', max_length=10),
        ),
        migrations.AlterField(
            model_name='discount',
            name='reason',
            field=models.CharField(choices=[('female', 'Female'), ('young', 'Young'), ('superuser', 'Superuser')], max_length=32),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('parent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.producttype')),
            ],
        ),
    ]