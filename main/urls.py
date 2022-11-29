from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.views.generic import TemplateView

schema_view = get_schema_view(
   openapi.Info(
      title="Rysgal API",
      default_version='v1',
      description="An api for ecommerce project.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gylyjov.rd@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('404/', TemplateView.as_view(template_name='404.html')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('auth/', TemplateView.as_view(template_name='auth.html')),
    path('cart/', TemplateView.as_view(template_name='cart.html')),
    path('contacts/', TemplateView.as_view(template_name='contacts.html')),
    path('interyer/', TemplateView.as_view(template_name='interyer.html')),
    path('like/', TemplateView.as_view(template_name='like.html')),
    path('login/', TemplateView.as_view(template_name='login.html')),
    path('media/', TemplateView.as_view(template_name='media.html')),
    path('profile/', TemplateView.as_view(template_name='profile.html')),
    path('search/', TemplateView.as_view(template_name='search.html')),
    path('services/', TemplateView.as_view(template_name='services.html')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("api/", include("api.urls")),
    path('admin/', admin.site.urls),
    path('<str:code>/', TemplateView.as_view(template_name='[id].html')),
    path('brand/<str:code>/', TemplateView.as_view(template_name='brand/[id].html')),
    path('category/<str:code>/', TemplateView.as_view(template_name='category/[id].html')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)