from django.shortcuts import render
from django.shortcuts import get_list_or_404, render

from .models import Producto

# Create your views here.

def index(request):
    producto_list = Producto.objects.order_by('nombre')[:6]
    context = {'product_list': producto_list}
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_list_or_404(Producto, pk=producto_id)
    return render(request,'producto.html', {'producto': producto})
