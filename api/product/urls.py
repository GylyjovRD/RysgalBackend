from django.urls import path

from . import views

urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name="product-list"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-main/', views.ProductMainList.as_view(), name="products-main"),
    path('design-samples/', views.SampleImageView.as_view(), name='design-samples'),
    path('design-samples-create/', views.SICreateView.as_view(), name='design-samples-create'),
    path('banners/', views.BannerListView.as_view(), name='banners'),
    path('background/', views.BackgroundView.as_view(), name='background'),
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('cashback/', views.CashbackView.as_view(), name="cashbat"),
    path('comment-create/', views.CommentCreateView.as_view(), name="comment-create"),
    path("stores/", views.StoresListView.as_view(), name="stores-list"),
    path('service/', views.ServicesView.as_view(), name="service"),
    path('contacts/', views.CompanySettingsView.as_view(), name="contacts"),
    path('user-agreement/', views.UserAgreementView.as_view(), name="user-agreement"),
    path('about-us/', views.AboutUsView.as_view(), name="about-us"),
    path('message/', views.MessagesView.as_view(), name="message"),
    path('rate/<int:pk>/', views.ProductRatingView.as_view(), name="rating"),
    path('user-ratings/', views.UserRatingsView.as_view(), name='user-ratings'),
    path('course/', views.CourseSettings.as_view(), name="course"),
    path('gif-banner/', views.GifBannerView.as_view(), name='gif-banner'),
    path('main-media/', views.MediaMainView.as_view(), name='main-media'),
    path('media-list/', views.MediaListView.as_view(), name='media-lilst'),
    path('media-seen-count/<int:pk>/', views.MediaSeenView.as_view(), name='media-seen-count'),
]