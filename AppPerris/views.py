from django.shortcuts import render



from .models import Rescatado


# Create your views here.
def paginaInicio(request):
    return render(request, 'index.html', {})


def contacto(request):
 return render(request, 'contacto.html', {})

def mostrarRescatados(request): 
    lista = Rescatado.objects.filter(estado="disponible")
    return render(request,'rescatados.html', {'lista':lista})



