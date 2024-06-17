from django.shortcuts import render,redirect
from .carro import Carro
from productos.models import Producto

# Create your views here.


def agregar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("carro:carro")


def eliminar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.eliminar_carrito(producto=producto)
    
    return redirect("carro:carro")



def restar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)
    
    return redirect("carro:carro")


def limpiar_carroproducto(request):
    carro= Carro(request)
    carro.limpiar_carrito()
    
    return redirect("carro:carro")


def carro_detalle(request):
    carro = Carro(request)
    productos_en_carro = carro.carro.items()

    return render(request, 'productos/carro_detalle.html', {'productos_en_carro': productos_en_carro})