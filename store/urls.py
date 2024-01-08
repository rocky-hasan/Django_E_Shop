from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('product-detail/<int:pk>/', views.Product_detail.as_view(), name='product_detail'),
    path('category/<str:foo>/', views.CategoryView.as_view(), name='category'),
]
