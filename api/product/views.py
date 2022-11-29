from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

from product.models import (Settings, Banner, Category, SubCategory, Brand, Product,
        Images, Attribute, Comments, SampleImages, Cashback, Stores, Services,
        CompanySettings, Messages, UserAgreement, AboutUs, ProductRating, GifBanner, 
        Medias, Background)


class BackgroundView(APIView):
    def get(self, request):
        background = Background.objects.all().last()
        serializer = BackgroundSerializer(background, many=False)
        return Response({"response":"success", "data":serializer.data})


class GifBannerView(APIView):
    def get(self, request):
        gifBanner = GifBanner.objects.all().last()
        serializer = GifBannerSerializer(gifBanner, many=False)
        return Response({"response":"success", "data":serializer.data})

class MediaMainView(APIView):
    def get(self, reqeust):
        main_media = Medias.objects.filter(is_main=True).last()
        serializer = MediaSerializer(main_media, many=False)
        return Response({"response":"success", "data":serializer.data})


class MediaListView(APIView, LimitOffsetPagination):
    def get(self, reqeust):
        medias = Medias.objects.all()
        data = self.paginate_queryset(medias, reqeust, view=self)
        serializer = MediaSerializer(data, many=True)
        response = self.get_paginated_response(serializer.data)
        return Response({"response": "success", "data": response.data}, status=status.HTTP_200_OK)

class MediaSeenView(APIView):
    def post(self, request, pk):
        try:
            selected_media = Medias.objects.get(pk=pk)
            selected_media.seen = selected_media.seen + 1
            selected_media.save()
            return Response({"response":"success"})
        except:
            return Response({"error":"Media could not be found."})

class CourseSettings(APIView):
    def get(self, request):
        course = Settings.objects.all().last()
        course = course.course
        course_obj = {}
        course_obj['course'] = course
        return Response({"response":"success", "data":course_obj})

class UserRatingsView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="***IMPORTANT*** Should be sent with token.")
    def get(self, request):
        user_id = request.user.id
        user_ratings = ProductRating.objects.filter(user=user_id)
        ratings = []
        for rating in user_ratings:
            ratings.append(rating.product.id)
        rating_list = {}
        rating_list['ratings'] = ratings
        return Response({"response":"success", "data":rating_list})

class ProductRatingView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="***IMPORTANT*** Should be sent with token.\n\nExample:\n{\"rating\":4}")
    def post(self, request, pk):
        user_id = request.user.id
        rating_product = ProductRating.objects.filter(product=pk, user=user_id).first()
        if rating_product:
            return Response({"response":"error"}, status=status.HTTP_403_FORBIDDEN)
        else:
            data = request.data
            data['user'] = user_id
            new_rating = data['rating']
            product = Product.objects.get(pk=pk)
            data['product'] = product.id
            rating_serializer = ProductRatingSerializer(data=data)
            if rating_serializer.is_valid():
                rating_serializer.save()
                new_average_rating = (product.rating_average * product.rating_count + new_rating)/(product.rating_count+1)
                product.rating_average = new_average_rating
                product.rating_count = product.rating_count + 1
                product.save()
                return Response({"response":"success"}, status=status.HTTP_200_OK)
            else:
                return Response({"response":"error"}, status=status.HTTP_400_BAD_REQUEST)


class CompanySettingsView(APIView):
    @swagger_auto_schema(responses={200: CompanySettingsSerializer})
    def get(self, request):
        try:
            company_info = CompanySettings.objects.all().order_by('id').last()
            serializer = CompanySettingsSerializer(company_info, many=False)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class UserAgreementView(APIView):
    @swagger_auto_schema(responses={200: UserAgreementSerializer})
    def get(self, request):
        try:
            company_info = UserAgreement.objects.all().order_by('id').last()
            serializer = UserAgreementSerializer(company_info, many=False)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class AboutUsView(APIView):
    @swagger_auto_schema(responses={200: AboutUsSerializer})
    def get(self, request):
        try:
            company_info = AboutUs.objects.all().order_by('id').last()
            serializer = AboutUsSerializer(company_info, many=False)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class MessagesView(APIView):
    @swagger_auto_schema(request_body=MessagesSerializer)
    def post(self, request):
        try:
            serializer = MessagesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response":"success", "message":"Hatyňyz üstünlikli ugradyldy."})
            else:
                return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class ServicesView(APIView):
    @swagger_auto_schema(responses={200: ServicesSerializer})
    def get(self, request):
        try:
            service = Services.objects.all().order_by('id').last()
            serializer = ServicesSerializer(service, many=False)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class StoresListView(APIView):
    @swagger_auto_schema(responses={200: StoresSerializer})
    def get(self, request):
        try:
            stores = Stores.objects.filter(is_active=True).order_by('id')
            serializer = StoresSerializer(stores, many=True)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    @swagger_auto_schema(request_body=CommentCreateSerializer)
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data._mutable = True
            data["user"] = user.id
            data._mutable = False
            serializer = CommentCreateSerializer(data=data)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response({"response":"success", "message":"Teswir üstünlikli ugradyldy"})
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class ProductMainList(APIView):
    @swagger_auto_schema(responses={200: ProductOutSerializer})
    def get(self, request):
        try:
            products = Product.objects.filter(is_main=True)[:4]
            serializer = ProductOutSerializer(products, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class CashbackView(APIView):
    @swagger_auto_schema(responses={200: CashbackOutSerializer})
    def get(self, request):
        try:
            cashback = Cashback.objects.all().last()
            serializer = CashbackOutSerializer(cashback, many=False)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class ProductListView(APIView, LimitOffsetPagination):
    param1 = openapi.Parameter('title_tm', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    param2 = openapi.Parameter('title_ru', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    param3 = openapi.Parameter('title_en', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    param4 = openapi.Parameter('byprice', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param5 = openapi.Parameter('bycreated', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param6 = openapi.Parameter('is_special', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param7 = openapi.Parameter('liked', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    param8 = openapi.Parameter('category', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    param9 = openapi.Parameter('brand', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    param10 = openapi.Parameter('is_new', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param11 = openapi.Parameter('is_discount', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param12 = openapi.Parameter('byrating', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    @swagger_auto_schema(manual_parameters=[param1, param2, param3, param4, param5, param12,param6, param7, param8, param9, param10, param11],
            operation_description="***IMPORTANT***: 'byprice','bycreated', 'byrating' should not be used together\n***IMPORTANT***: 'liked' should be list of ids comma saparated. ex: ?liked=21,22,23",
            responses={200: ProductOutSerializer})
    def get(self, request):
        title_tm = request.query_params.get('title_tm', None)
        title_ru = request.query_params.get('title_ru', None)
        title_en = request.query_params.get('title_en', None)
        byprice = request.query_params.get('byprice', None)
        bycreated = request.query_params.get('bycreated', None)
        byrating = request.query_params.get('byrating', None)
        is_special = request.query_params.get('is_special', None)
        is_new = request.query_params.get('is_new', None)
        is_discount = request.query_params.get('is_discount', None)
        liked = request.query_params.get('liked', None)
        category = request.query_params.get('category', None)
        brand = request.query_params.get('brand', None)
        if byprice == 'true':
            byprice = True
        if byprice == 'false':
            byprice = False
        if bycreated == 'true':
            bycreated = True
        if bycreated == 'false':
            bycreated = False
        if is_special == 'true':
            is_special = True
        if is_special == 'false':
            is_special = False
        if is_new == 'true':
            is_new = True
        if is_new == 'false':
            is_new = False
        if is_discount == 'true':
            is_discount = True
        if is_discount == 'false':
            is_discount = False
        if byrating == 'true':
            byrating = True
        if byrating == 'false':
            byrating = False
        dliked = []
        if liked:
            liked = liked.split(',')
            for l in liked:
                if l.isdecimal():
                    dliked.append(int(l))

        try:
            products = Product.objects.filter(is_active=True).order_by('-created_at')
            if title_tm:
                products = products.filter(title_tm__icontains=title_tm)
            if title_ru:
                products = products.filter(title_ru__icontains=title_ru)
            if title_en:
                products = products.filter(title_en__icontains=title_en)
            if category:
                products = products.filter(subcategory=category)
            if brand:
                products = products.filter(brand=brand)
            if is_special == True:
                products = products.filter(is_special=is_special)
            if is_special == False:
                products = products.filter(is_special=is_special)
            if is_new == True:
                products = products.filter(is_new=is_new)
            if is_new == False:
                products = products.filter(is_new=is_new)
            if is_discount == True:
                products = products.filter(discount__gt=0)
            if is_discount == False:
                products = products.filter(discount=0)
            if byprice == True:
                products = sorted(products, key=lambda p: p.get_price())
            if byprice == False:
                products = sorted(products, key=lambda p: p.get_price(), reverse=True)
            if bycreated == True:
                products = products.order_by('created_at')
            if bycreated == False:
                products = products.order_by('-created_at')
            if byrating == False:
                products = products.order_by('rating_average')
            if byrating == True:
                products = products.order_by('-rating_average')
            if len(dliked) > 0:
                products = products.filter(pk__in=dliked)
            
            data = self.paginate_queryset(products, request, view=self)
            serializer = ProductOutSerializer(data, many=True)
            response = self.get_paginated_response(serializer.data)
            return Response({"response": "success", "data": response.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    @swagger_auto_schema(responses={200: ProductDetailSerializer})
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductDetailSerializer(product)
            cat_id = product.subcategory.id
            cat_products = Product.objects.filter(subcategory=cat_id).exclude(id=product.id)[:8]
            spserializer = ProductOutSerializer(cat_products, many=True)
            services = Services.objects.all().order_by('-id').first()
            service_serializer = ServicesProductSerializer(services, many=False)
            return Response({"response": "success", "data": serializer.data, "similar_products":spserializer.data, "services":service_serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class SampleImageView(APIView):
    @swagger_auto_schema(responses={200: SampleImageSerializer})
    def get(self, request):
        try:
            samples = SampleImages.objects.filter(is_active=True)[:12]
            serializer = SampleImageSerializer(samples, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)
    
class SICreateView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]
    @swagger_auto_schema(request_body=SampleImageSerializer, responses={200: SampleImageSerializer})
    def post(self, request):
        try:
            data = request.data
            serializer = SampleImageInSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class BannerListView(APIView):
    @swagger_auto_schema(responses={200: BannerListSerializer})
    def get(self, request):
        try:
            banners = Banner.objects.filter(is_active=True).order_by('-id')[:3]
            serializer = BannerListSerializer(banners, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class BrandListView(APIView):
    @swagger_auto_schema(responses={200: BrandSerializer})
    def get(self, request):
        try:
            brands = Brand.objects.all()
            serializer = BrandSerializer(brands, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class CategoryListView(APIView):
    @swagger_auto_schema(responses={200:CategoryListSerializer})
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategoryListSerializer(categories, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)