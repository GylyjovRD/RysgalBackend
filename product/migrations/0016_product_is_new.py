# Generated by Django 3.2 on 2022-08-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20220801_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='Täzemi?'),
        ),
    ]
