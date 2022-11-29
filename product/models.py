from django.db import models
from api.utils import get_random_string
from django.contrib.auth.models import User
from PIL import Image

WEB_IMAGE = 512
MOBILE_IMAGE = 256

class Settings(models.Model):
    course = models.FloatField(default=1, verbose_name="Kurs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.course) + str(self.created_at)

    class Meta:
        verbose_name = "Sazlama"
        verbose_name_plural = "Sazlamalar"

class Cashback(models.Model):
    title = models.CharField(max_length=255,verbose_name="Ady")
    start_date = models.DateField(verbose_name="Başlaýan wagty")
    end_date = models.DateField(verbose_name="Gutarýan wagty")
    amount = models.FloatField(default=0, verbose_name="Summa")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Keşbek"
        verbose_name_plural = "Keşbeklar"
    

def general_image(instance, filename):
    rand = get_random_string()
    return 'general/{rand}-{filename}'.format(rand=rand, filename=filename)

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    image = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Surat")
    image_mobile = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Mobil Surat")
    is_active = models.BooleanField(default=True, verbose_name="Aktiwmy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"

class SampleImages(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    image = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Surat")
    image_mobile = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Mobil Surat")
    is_active = models.BooleanField(default=True, verbose_name="Aktiwmy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >512 or img.width > 512:
            new_img = (512, 512)
            img.thumbnail(new_img)
            img.save(self.image.path)

        img_mobile = Image.open(self.image_mobile.path)
        if img_mobile.height >WEB_IMAGE or img_mobile.width > WEB_IMAGE:
            new_img = (WEB_IMAGE, WEB_IMAGE)
            img_mobile.thumbnail(new_img)
            img_mobile.save(self.image_mobile.path)
    
    class Meta:
        verbose_name = "Nusga Surat"
        verbose_name_plural = "Nusga Suratlar"

class Category(models.Model):
    title_tm = models.CharField(max_length=255, verbose_name="Tm-Ady")
    title_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ru-Ady")
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="En-Ady")
    image = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Surat")
    image_mobile = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Mobil Surat")

    def __str__(self):
        return self.title_tm
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >WEB_IMAGE or img.width > WEB_IMAGE:
            new_img = (WEB_IMAGE, WEB_IMAGE)
            img.thumbnail(new_img)
            img.save(self.image.path)

        img_mobile = Image.open(self.image_mobile.path)
        if img_mobile.height >MOBILE_IMAGE or img_mobile.width > MOBILE_IMAGE:
            new_img = (MOBILE_IMAGE, MOBILE_IMAGE)
            img_mobile.thumbnail(new_img)
            img_mobile.save(self.image_mobile.path)
    
    class Meta:
        verbose_name = "Kategoriýa"
        verbose_name_plural = "Kategoriýalar"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_sub', verbose_name="Kategoriýa")
    title_tm = models.CharField(max_length=255, verbose_name="Tm-Ady")
    title_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ru-Ady")
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="En-Ady")
    description_tm = models.TextField(null=True, blank=True, verbose_name="Tm-Giňişleýin")
    description_ru = models.TextField(null=True, blank=True, verbose_name="Ru-Giňişleýin")
    description_en = models.TextField(null=True, blank=True, verbose_name="En-Giňişleýin")

    def __str__(self):
        return self.title_tm
    
    class Meta:
        verbose_name = "Içki Kategoriýa"
        verbose_name_plural = "Içki Kategoriýalar"

class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    image = models.ImageField(upload_to=general_image, default='general/default.jpg', verbose_name="Surat", help_text="Bu suratyň ölçegleri 64x64 bolmaly!")

    def __str__(self):
        return self.title
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >MOBILE_IMAGE or img.width > MOBILE_IMAGE:
            new_img = (MOBILE_IMAGE, MOBILE_IMAGE)
            img.thumbnail(new_img)
            img.save(self.image.path)
    
    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"

def product_image(instance, filename):
    rand = get_random_string()
    return 'products/{rand}-{filename}'.format(rand=rand, filename=filename)

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, 
            null=True, blank=True, related_name='subcategory_product', verbose_name="Içki kategoriýa")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,
            null=True, blank=True, verbose_name="Brendy")
    title_tm = models.CharField(max_length=255, verbose_name="TM-Ady")
    title_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ru-Ady")
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="En-Ady")
    main_image = models.ImageField(upload_to=product_image, default='products/default.png', verbose_name="Suraty")
    main_image_mobile = models.ImageField(upload_to=product_image, default='products/default_mobile.png', verbose_name="Mobil Suraty")
    description_tm = models.TextField(null=True, blank=True, verbose_name="Tm-Giňişleýin")
    description_ru = models.TextField(null=True, blank=True, verbose_name="Ru-Giňişleýin")
    description_en = models.TextField(null=True, blank=True, verbose_name="En-Giňişleýin")
    price = models.FloatField(default=0, verbose_name="Bahasy")
    discount = models.PositiveIntegerField(default=0)
    is_usd = models.BooleanField(default=False, verbose_name="Dollardamy?")
    is_new = models.BooleanField(default=False, verbose_name="Täzemi?")
    is_main = models.BooleanField(default=False, verbose_name="Baş sahypadamy?")
    is_special = models.BooleanField(default=False, verbose_name="Ýöritemi?")
    is_active = models.BooleanField(default=True, verbose_name="Ulanyşdamy")
    rating_average = models.FloatField(default=0)
    rating_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_tm
    
    def save(self):
        super().save()
        img = Image.open(self.main_image.path)
        if img.height >WEB_IMAGE or img.width > WEB_IMAGE:
            new_img = (WEB_IMAGE, WEB_IMAGE)
            img.thumbnail(new_img)
            img.save(self.main_image.path)

        img_mobile = Image.open(self.main_image_mobile.path)
        if img_mobile.height >MOBILE_IMAGE or img_mobile.width > MOBILE_IMAGE:
            new_img = (MOBILE_IMAGE, MOBILE_IMAGE)
            img_mobile.thumbnail(new_img)
            img_mobile.save(self.main_image_mobile.path)

    def get_old_price(self):
        course = Settings.objects.latest('id')
        usd_price = round(float(self.price * course.course))
        if self.is_usd == True:
            return usd_price
        else:
            return self.price
    
    def get_price(self):
        course = Settings.objects.latest('id')
        usd_price = round(float(self.price * course.course))
        if self.is_usd == True:
            if self.discount > 0:
                return int(usd_price - (usd_price/self.discount))
            else:
                return int(usd_price)
        else:
            if self.discount > 0:
                return int(self.price - (self.price/self.discount))
            else:
                return int(self.price)
    
    class Meta:
        verbose_name = "Haryt"
        verbose_name_plural = "Harytlar"

class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratinglar"
    
    def __str__(self):
        return str(self.user.username) + "-" + str(self.product.title_tm)

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
            related_name='product_image')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=product_image, default='products/default.jpg')
    image_mobile = models.ImageField(upload_to=product_image, default='products/default.jpg')

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >WEB_IMAGE or img.width > WEB_IMAGE:
            new_img = (WEB_IMAGE, WEB_IMAGE)
            img.thumbnail(new_img)
            img.save(self.image.path)

        img_mobile = Image.open(self.image_mobile.path)
        if img_mobile.height >MOBILE_IMAGE or img_mobile.width > MOBILE_IMAGE:
            new_img = (MOBILE_IMAGE, MOBILE_IMAGE)
            img_mobile.thumbnail(new_img)
            img_mobile.save(self.image_mobile.path)

    class Meta:
        verbose_name = "Surat"
        verbose_name_plural = "Suratlar"

class Attribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attribute', verbose_name="Haryt")
    title_tm = models.CharField(max_length=255, verbose_name="Tm-Ady")
    title_ru = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ru-Ady")
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="En-Ady")
    description_tm = models.TextField(null=True, blank=True, verbose_name="Tm-giňişleýin")
    description_ru = models.TextField(null=True, blank=True, verbose_name="Ru-giňişleýin")
    description_en = models.TextField(null=True, blank=True, verbose_name="En-giňişleýin")

    def __str__(self):
        return self.title_tm

    class Meta:
        verbose_name = "Atribýut"
        verbose_name_plural = "Atribýutlar"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
            related_name='user_comment', verbose_name="Ulanyjy")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
            related_name='product_comment', verbose_name="Haryt")
    title = models.CharField(max_length=255, verbose_name="Ady")
    image = models.ImageField(upload_to="comments/", null=True, blank=True, verbose_name="Surat")
    description = models.TextField(null=True, blank=True, verbose_name="Giňişleýin")
    is_active = models.BooleanField(default=False, verbose_name="Aktiwmy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Comments, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height >WEB_IMAGE or img.width > WEB_IMAGE:
                new_img = (WEB_IMAGE, WEB_IMAGE)
                img.thumbnail(new_img)
                img.save(self.image.path)
    
    class Meta:
        verbose_name = "Teswir"
        verbose_name_plural = "Teswirler"

class Stores(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    description = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=64, verbose_name="Telefon")
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name="Email")
    image = models.ImageField(upload_to='stores/', null=True, blank=True, verbose_name="Surat")
    image_mobile = models.ImageField(upload_to='stores/', null=True, blank=True, verbose_name="Mobil Surat")
    address = models.TextField(null=True, verbose_name="Adres")
    map_image_mobile = models.ImageField(upload_to='stores/', null=True, blank=True, verbose_name="Karta Surat")
    map_url = models.TextField(null=True, blank=True, verbose_name="Karta Link")
    is_active = models.BooleanField(default=True, verbose_name="Aktiwmy?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dükan"
        verbose_name_plural = "Dükanlar"

class DeliveryOption(models.Model):
    icon = models.ImageField(upload_to="stores/")

class Services(models.Model):
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_tm = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    icon_1 = models.ImageField(upload_to="stores/", null=True, blank=True)
    content_1_tm = models.CharField(max_length=255, null=True, blank=True)
    content_1_ru = models.CharField(max_length=255, null=True, blank=True)
    content_1_en = models.CharField(max_length=255, null=True, blank=True)
    icon_2 = models.ImageField(upload_to="stores/", null=True, blank=True)
    content_2_tm = models.CharField(max_length=255, null=True, blank=True)
    content_2_ru = models.CharField(max_length=255, null=True, blank=True)
    content_2_en = models.CharField(max_length=255, null=True, blank=True)
    icon_3 = models.ImageField(upload_to="stores/", null=True, blank=True)
    content_3_tm = models.CharField(max_length=255, null=True, blank=True)
    content_3_ru = models.CharField(max_length=255, null=True, blank=True)
    content_3_en = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title_tm

    def save(self, *args, **kwargs):
        super(Services, self).save(*args, **kwargs)
        if self.icon_1:
            img1 = Image.open(self.icon_1.path)
            if img1.height >64 or img1.width > 64:
                new_img = (64, 64)
                img1.thumbnail(new_img)
                img1.save(self.icon_1.path)
        if self.icon_2:
            img2 = Image.open(self.icon_2.path)
            if img2.height >64 or img2.width > 64:
                new_img = (64, 64)
                img2.thumbnail(new_img)
                img2.save(self.icon_2.path)

        if self.icon_3:
            img3 = Image.open(self.icon_3.path)
            if img3.height >64 or img3.width > 64:
                new_img = (64, 64)
                img3.thumbnail(new_img)
                img3.save(self.icon_3.path)

    class Meta:
        verbose_name = "Serwis"
        verbose_name_plural = "Serwislar"

class CompanySettings(models.Model):
    title = models.CharField(max_length=255, default="Aragatnaşyk")
    mobile = models.CharField(max_length=64)
    imo = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    instagram = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Aragatnaşyk maglumat"
        verbose_name_plural = "Aragatnaşyk maglumatlary"

class Messages(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=64)
    email = models.CharField(max_length=128, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hat"
        verbose_name_plural = "Hatlar"
        ordering = ('created_at', )

class UserAgreement(models.Model):
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_tm

    class Meta:
        verbose_name = "Ulanyş Düzgüni"
        verbose_name_plural = "Ulanyş Düzgünleri"

class AboutUs(models.Model):
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_tm

    class Meta:
        verbose_name = "Biz Barada"
        verbose_name_plural = "Biz Barada"

class GifBanner(models.Model):
    title = models.CharField(max_length=255, default='Gif Image')
    image = models.ImageField(upload_to="general/")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gif Banner"
        verbose_name_plural = "Gif Bannerlar"

class Medias(models.Model):
    title_tm = models.CharField(max_length=255, default="Media")
    title_ru = models.CharField(max_length=255, default="Media")
    title_en = models.CharField(max_length=255, default="Media")
    is_main = models.BooleanField(default=False)
    description_tm = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="videos/", null=True, default="videos/default.jpg", verbose_name="Surat")
    image_mobile = models.ImageField(upload_to="videos/", null=True, default="videos/default.jpg", verbose_name="Surat Mobile")
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video")
    video_mobile = models.FileField(upload_to='videos/', null=True, verbose_name="Video Mobile")
    seen = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_tm

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medialar"

class Background(models.Model):
    bg_main = models.ImageField(upload_to="general/", null=True, blank=True, verbose_name="Esasy Background")
    bg_image1 = models.ImageField(upload_to="general/", verbose_name="Bolek Background1")
    bg_image2 = models.ImageField(upload_to="general/", null=True, blank=True, verbose_name="Bolek Background2")
    bg_image3 = models.ImageField(upload_to="general/", null=True, blank=True, verbose_name="Bolek Background3")
    bg_image4 = models.ImageField(upload_to="general/", null=True, blank=True, verbose_name="Bolek Background4")
    bg_image5 = models.ImageField(upload_to="general/", null=True, blank=True, verbose_name="Bolek Background5")

    def __str__(self):
        return "bg_image"
    
    class Meta:
        verbose_name = "Arka Surat"
        verbose_name_plural = "Arka Suratlar"