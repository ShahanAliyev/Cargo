import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator('^\\d{7}$', message='Please enter your valid phone number')]),
        ),
    ]
