# Generated by Django 3.2 on 2022-07-27 04:38

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_cashback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashback',
            name='amount',
            field=models.FloatField(default=0, verbose_name='Summa'),
        ),
        migrations.AlterField(
            model_name='cashback',
            name='end_date',
            field=models.DateField(verbose_name='Gutarýan wagty'),
        ),
        migrations.AlterField(
            model_name='cashback',
            name='start_date',
            field=models.DateField(verbose_name='Başlaýan wagty'),
        ),
        migrations.AlterField(
            model_name='cashback',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Ady'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='products/default.png', upload_to=product.models.product_image, verbose_name='Suraty'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image_mobile',
            field=models.ImageField(default='products/default_mobile.png', upload_to=product.models.product_image, verbose_name='Mobil Suraty'),
        ),
    ]
