# Generated by Django 3.2 on 2022-08-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_average',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
