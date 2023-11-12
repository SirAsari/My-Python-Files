# marketplace/views.py
from django.shortcuts import render

def admin_page(request):
    # Add logic to handle admin page
    return render(request, 'marketplace/admin_page.html')

def home_page(request):
    # Add logic to handle home page
    return render(request, 'marketplace/home_page.html')

def detail_page(request, barang_id):
    # Add logic to handle detail page
    return render(request, 'marketplace/detail_page.html')

def cart_page(request):
    # Add logic to handle cart page
    return render(request, 'marketplace/cart_page.html')
