from rest_framework import serializers

from product.models import (Settings, Banner, Category, SubCategory, Brand, Product,
        Images, Attribute, Comments, SampleImages, Cashback, Stores, Services,
        CompanySettings, Messages, UserAgreement, AboutUs, ProductRating, GifBanner, 
        Medias, Background)

class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = "__all__"

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = "__all__"

class CompanySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySettings
        fields = "__all__"
    
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"

class UserAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAgreement
        fields = "__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        # fields = ["id", "title", "description"]
        fields = "__all__"

class ServicesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        # fields = ["icon_1", "content_1", "icon_2", "content_2", "icon_3", "content_3"]
        fields = "__all__"

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = "__all__"

class CashbackOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = "__all__"

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductOutSerializer(serializers.ModelSerializer):
    rating_average = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ["id", 'title_tm', 'title_ru', 'title_en', 'main_image', 'main_image_mobile', 
                'description_tm', 'description_ru', 'description_en','get_price', 'is_special', 
                'is_new','created_at', 'discount', 'rating_average', 'rating_count']
    
    def get_rating_average(self, obj):
        rating = round(obj.rating_average, 2)
        return rating

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        # fileds = ["id", "title", "description", "created_at"]

class SampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleImages
        fields = '__all__'

class SampleImageInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleImages
        # fields = ['id', 'image', 'image_mobile']
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    image_list = ProductImageSerializer(many=True, source='product_image')
    attributes = ProductAttributeSerializer(many=True, source='product_attribute')
    # comments = ProductCommentSerializer(many=True, source='product_comment')
    # price = serializers.SerializerMethodField('get_price')
    price = serializers.IntegerField(source="get_price")
    old_price = serializers.IntegerField(source="get_old_price")
    comments = serializers.SerializerMethodField(read_only=True)
    subcategory = SubCategorySerializer(many=False)
    brand = BrandSerializer(many=False)
    # services = serializers.SerializerMethodField(read_only=True)
    rating_average = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title_tm', 'title_ru', 'title_en', 'main_image', 'main_image_mobile', 
                'description_tm', 'description_ru', 'description_en', 'price', 'old_price', 'discount',
                'rating_average', 'rating_count', 'is_usd', 'is_special', 'subcategory', 'brand', 
                'image_list', 'attributes', 'comments']
    
    def get_rating_average(self, obj):
        rating = round(obj.rating_average, 2)
        return rating
    
    def get_price(self, obj):
        price = obj.get_price
        return price

    def get_comments(self, obj):
        comments = Comments.objects.filter(product=obj.id, is_active=True)
        serializer = ProductCommentSerializer(comments, many=True)
        return serializer.data
    
    # def get_services(self):
    #     service = Services.objects.all().order_by('-id').first()
    #     serializer = ServicesProductSerializer(service, many=False)
    #     return serializer.data

class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    subcategories=CategorySerializer(many=True, source="category_sub")
    class Meta:
        model = Category
        fields = ['id', 'title_tm', 'title_ru', 'title_en', 'image', 'image_mobile', 'subcategories']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class GifBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GifBanner
        fields = "__all__"

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medias
        fields = "__all__"