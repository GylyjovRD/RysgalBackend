from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from api.utils import get_random_string

class Mobile(models.Model):
    mobile = models.CharField(max_length=16)
    is_sms_sent = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    sms_code = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mobile
    
    class Meta:
        ordering = ['-created_at']

def upload_to(instance, filename):
    rand = get_random_string()
    return 'profiles/{rand}{filename}'.format(rand=rand, filename=filename)

class Profile(models.Model):
    REGION = [
        ('Asgabat', "Asgabat"),
        ('Ahal', "Ahal"),
        ('Balkan', 'Balkan'),
        ('Dashoguz', 'Dashoguz'),
        ('Lebap', 'Lebap'),
        ('Mary', 'Mary')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", verbose_name="Ulanyjy")
    image = models.ImageField(("Surat"), upload_to=upload_to, default="profiles.png")
    mobile = models.CharField(max_length=255, null=True, blank=True, verbose_name="Telefon belgi")
    fullname = models.CharField(max_length=255, null=True, blank=True, verbose_name="Doly adyňyz")
    email = models.CharField(max_length=128, null=True, blank=True, verbose_name="Elektron Poçta")
    region = models.CharField(max_length=64, choices=REGION, default='Asgabat', verbose_name="Welaýat")
    address_line_1 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Adres - setir 1")
    address_line_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Adres - setir 2")
    balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering = ['-created_at']

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profiller"