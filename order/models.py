from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    STATUS = [
        ('ORDERPLACED', 'ORDERPLACED'),
        ('ACCEPTED', 'ACCEPTED'),
        ('DECLINED', 'DECLINED'),
        ('SHIPPED', 'SHIPPED'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNED', 'RETURNED'),
    ]
    PAYMENT = [
        ('TERMINAL', 'TERMINAL'),
        ('NAGT', 'NAGT'),
    ]
    REGION = [
        ('Asgabat', "Asgabat"),
        ('Ahal', "Ahal"),
        ('Balkan', 'Balkan'),
        ('Dashoguz', 'Dashoguz'),
        ('Lebap', 'Lebap'),
        ('Mary', 'Mary')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders', verbose_name="Ulanyjy")
    status = models.CharField(max_length=64, choices=STATUS, default='ORDERPLACED', verbose_name="Sargyt ýagdaýy")
    payment_type = models.CharField(max_length=16, choices=PAYMENT, default='NAGT', verbose_name='Töleg görnüşi')
    region = models.CharField(max_length=64,choices=REGION, default='Asgabat', verbose_name="Welaýat")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Adres")
    total_price = models.FloatField(default=0, verbose_name="Jemi summa")
    is_active = models.BooleanField(default=True, verbose_name="Aktiwmy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username) + '-' + str(self.total_price)

    class Meta:
        verbose_name = "Sargyt"
        verbose_name_plural = "Sargytlar"
        ordering = ['-created_at']

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_products', verbose_name="Sargyt")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,related_name='product_orders', verbose_name="Haryt")
    product_price = models.FloatField(default=0, verbose_name="Bahasy")
    qty = models.IntegerField(default=0, verbose_name="Sany")

    def __str__(self):
        return str(self.product.title_tm) + '-' + str(self.order.user.username)

    class Meta:
        verbose_name = "Sargyt Haryt"
        verbose_name_plural = "Sargyt Harytlary"