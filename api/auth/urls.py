from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('register/', views.registerUser, name="register"),
    path('profile-create/', views.ProfileCreateView.as_view(), name="profile-create"),
    path("profile-delete/<int:pk>/", views.ProfileDelete.as_view(), name="profile-delete"),
    path("reset-password/", views.reset_password, name='reset_password'),
    path("register-mobile/", views.registerMobile, name="register-mobile"),
    path("sms-list/", views.smsList, name="sms-list"),
    path("resend-sms/", views.resendSms, name="resend-sms"),
    path("verify-code/", views.verifyCode, name="verify-code"),
]