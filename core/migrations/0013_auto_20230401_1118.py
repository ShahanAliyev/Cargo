# Generated by Django 3.2 on 2023-04-01 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'FAQ Category',
                'verbose_name_plural': 'FAQ Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Deactive')], default=1)),
                ('order', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.categoryfaq')),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
