from django.contrib import messages



def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if "carro" in request.session:
            for key, value in request.session["carro"].items():
                total += int(value['total_unit'])
        else:
            messages.error(request, "No hay productos en el carrito")
    else:
        messages.error(request, "Para ver carrito, debe iniciar sesión")
    return {'importe_total_carro': total}