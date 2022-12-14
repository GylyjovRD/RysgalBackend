# Generated by Django 3.2 on 2022-07-25 12:58

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adres - setir 1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adres - setir 2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Elektron Poçta'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Doly adyňyz'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='prifiles', upload_to=authentication.models.upload_to, verbose_name='Surat'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefon belgi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.IntegerField(choices=[(1, 'Asgabat'), (2, 'Ahal'), (3, 'Balkan'), (4, 'Dashoguz'), (5, 'Lebap'), (6, 'Mary')], default=1, verbose_name='Welaýat'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Ulanyjy'),
        ),
    ]
