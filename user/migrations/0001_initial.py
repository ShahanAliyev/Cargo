# Generated by Django 3.2 on 2023-03-16 20:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Man'), ('W', 'Woman')], max_length=1)),
                ('phone', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^\\d{7}$', message='Please enter your valid phone number')])),
                ('gov_prefix', models.CharField(choices=[('AZE', 'AZE'), ('AA', 'AA'), ('MYI', 'MYI'), ('DYI', 'DYI')], max_length=3)),
                ('gov_id', models.CharField(max_length=8)),
                ('fin_code', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9,A-Z,a-z]{7}$', message='Fin Code has to be 7 characters with letters and digits')])),
                ('client_code', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('monthly_expences', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('birth_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('phone_prefix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.phoneprefix')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.warehouse')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
