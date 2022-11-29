from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from datetime import datetime
import random
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import (UserSerializerWithToken, UserResgisterSerializer, 
                        UserOutSerializer, ProfileCreateSerializer, 
                        ProfileOutSerializer, MobileSerializer, RegisterMobileSerializer,
                        MobileVerifySerializer)

from authentication.models import Profile, Mobile
from product.models import Cashback

@swagger_auto_schema(methods=["POST"], request_body=RegisterMobileSerializer)
@api_view(['POST'])
def registerMobile(request):
    data = request.data
    generated_code = random.randint(1000, 9999)
    data['sms_code'] = generated_code
    oldMobile = Mobile.objects.filter(mobile=data['mobile']).first()
    if oldMobile:
        oldMobile.delete()

    try:
        serializer = MobileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"success", "message":"Telefon belginizi tassyklamagynyz ucin sms ugradyldy."})
    except:
        return Response({"response":"error"})

@swagger_auto_schema(methods=["GET"], responses={200: MobileSerializer})
@api_view(['GET'])
def smsList(request):
    tMobiles = Mobile.objects.filter(is_sms_sent=False)
    mobiles = tMobiles.filter(is_verified=False)
    for mobile in mobiles:
        mobile.is_sms_sent = True
        mobile.save()
    serializer = MobileVerifySerializer(mobiles, many=True)
    return Response({'response':'success', 'data':serializer.data})

@swagger_auto_schema(methods=["POST"], request_body=RegisterMobileSerializer)
@api_view(["POST"])
def resendSms(request):
    data = request.data
    mobile = Mobile.objects.get(mobile=data["mobile"])
    mobile.is_sms_sent = False
    mobile.save()
    return Response({"response":"success", "message":"New sms have been sent"})

@swagger_auto_schema(methods=["POST"], request_body=MobileVerifySerializer)
@api_view(['POST'])
def verifyCode(request):
    data = request.data
    mobile = Mobile.objects.filter(mobile=data["mobile"]).first()
    if mobile.sms_code == data["sms_code"]:
        mobile.is_verified = True
        mobile.save()
        return Response({"response":"success", "message":"Mobile verified successfully!"})
    else:
        return Response({"response":"error", "message":"Wrong code."})


class LoginUser(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

register_response = openapi.Response("response")
@swagger_auto_schema(methods=["POST"], request_body=UserResgisterSerializer,
        responses={200: UserSerializerWithToken(many=False)})
@api_view(['POST'])
def registerUser(request):
    data = request.data
    mobile = Mobile.objects.filter(mobile=data["username"]).first()
    if not mobile:
        return Response({"response":"error", "message":"Telefon belgiňizi tassyklaň"})
    elif mobile.is_verified == True: 
        try:
            user = User.objects.create(
                username = data["username"],
                password = make_password(data["password"])
            )
            serializer = UserSerializerWithToken(user, many=False)
            data['user'] = user.id
            data['mobile'] = user.username
            cashback = Cashback.objects.all().last()
            register_date = datetime.now().date()
            if register_date <= cashback.end_date and register_date >= cashback.start_date:
                data['balance'] = cashback.amount
            else:
                data['balance'] = 0
            profile_serializer = ProfileCreateSerializer(data=data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response({"response":"success", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"response":"error", "message":"Profile could not be created."})
        except:
            return Response({"response":"error", "message":"User already registered."})
    else:
        return Response({"response":"error", "message":"Telefon belgiňizi tassyklaň"})

@swagger_auto_schema(methods=["POST"], operation_description="***IMPORTANT*** Should be sent with token.\n\nExample:\n{\"password\":\"somepassword\"}")
@api_view(['POST'])
def reset_password(request):
    data = request.data
    try:
        user = request.user
        user.password = make_password(data["password"])
        user.save()
        serializer = UserSerializerWithToken(user, many=False)
        return Response({"response":"success", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
    except:
        return Response({"response":"error"})

class ProfileCreateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(responses={200: ProfileOutSerializer})
    def get(self, request):
        try:
            user = request.user
            profile = Profile.objects.filter(user=user).first()
            serializer = ProfileOutSerializer(profile, many=False)
            return Response({"response":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"response":"error"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProfileCreateSerializer)
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data._mutable = True
            data["user"] = user.id
            data._mutable = False
            serializer = ProfileCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response":"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProfileCreateSerializer)
    def put(self, request):
        try:
            user = request.user
            data = request.data
            data._mutable = True
            data['user'] = user.id
            data._mutable = False
            profile = Profile.objects.get(user=user)
            serializer = ProfileCreateSerializer(profile, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response":"success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response":"error"}, status=status.HTTP_404_NOT_FOUND)

class ProfileDelete(APIView):
    permission_classes = [IsAdminUser]
    def delete(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            profile.delete()
            return Response({"response": "success"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"response": "error"}, status=status.HTTP_403_FORBIDDEN)