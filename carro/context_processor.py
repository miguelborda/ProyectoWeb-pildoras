from carro.carro import Carro

def importe_total_carro(request):
    carro=Carro(request)
    total=125
    print(request.session)
    if request.user.is_authenticated:
        for key,value in request.session["carro"].items():
            total=total+(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}