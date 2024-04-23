from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.

def product_list(request):
  products = Product.objects.all()
  return render(request, 'products/list.html', {'products': products})


def product_detail(request, id):
  product = get_object_or_404(Product, id=id)
  return render(request, 'products/detail.html', {'product': product})