# Generated by Django 3.2 on 2022-07-25 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0009_cashback'),
        ('order', '0004_auto_20220725_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Aktiwmy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ORDERPLACED', 'ORDERPLACED'), ('ACCEPTED', 'ACCEPTED'), ('DECLINED', 'DECLINED'), ('SHIPPED', 'SHIPPED'), ('DELIVERED', 'DELIVERED'), ('RETURNED', 'RETURNED')], default='ORDERPLACED', max_length=64, verbose_name='Sargyt ýagdaýy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Jemi summa'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='Ulanyjy'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='order.order', verbose_name='Sargyt'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_orders', to='product.product', verbose_name='Haryt'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='product_price',
            field=models.FloatField(default=0, verbose_name='Bahasy'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='qty',
            field=models.IntegerField(default=0, verbose_name='Sany'),
        ),
    ]
