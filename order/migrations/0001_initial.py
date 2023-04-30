from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_alter_faq_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('next_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.status')),
            ],
        ),
    ]
