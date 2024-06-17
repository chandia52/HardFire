from django.shortcuts import render,redirect

from django.http import HttpResponse

from productos.models import Producto,Categoria

from django.views.generic import DetailView

from productos.models import Producto

# Create your views here.

def home(request):
    productos = Producto.objects.order_by('?')[:4]
    http_response = render(
        request=request,
        template_name="productos/home.html",
        context={'productos':productos},
    )
    return http_response

def listar_productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'categorias': categorias, 'productos': productos})

def categorias(request):
    contexto = {
        'categorias': Categoria.objects.all()
    }
    http_response = render(
        request=request,
        template_name="productos/listar_productos.html",
        context=contexto,
    )
    return http_response

def categorias(request):
    contexto = {
        'categorias': Categoria.objects.all()
    }
    http_response = render(
        request=request,
        template_name="productos/categorias.html",
        context=contexto,
    )
    return http_response

def categoria_detail(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoria_id)
    productos = categoria.producto.all()
    return render(request, 'productos/categoria_detail.html', {'categoria': categoria, 'productos': productos,'categorias':categorias, })

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/product_detail.html"

def buscar(request):
    query = request.GET.get('q')
    products = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'productos/buscar.html', {'products':products})
