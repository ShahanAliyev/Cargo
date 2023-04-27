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
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('discounted_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cost_azn', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('discounted_cost_azn', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_liquid', models.BooleanField(default=False)),
                ('shop_name', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/declaration/')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('weight', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('penalty_status', models.BooleanField(default=False)),
                ('penalty', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declarations', to='core.country')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency')),
                ('discount', models.ManyToManyField(blank=True, related_name='declarations', to='core.Discount')),
                ('product_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='declarations', to='core.currency')),
                ('product_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='declarations', to='core.producttype')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='declarations', to='order.status')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='declarations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
