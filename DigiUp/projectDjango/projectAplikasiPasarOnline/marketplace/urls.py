# marketplace/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_page, name='admin_page'),
    path('home/', views.home_page, name='home_page'),
    path('detail/<int:barang_id>/', views.detail_page, name='detail_page'),
    path('cart/', views.cart_page, name='cart_page'),
]
