from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Rescatado
from django.contrib.auth import logout as do_logout

from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
from django.http import HttpResponse
from django.forms import inlineformset_factory






# Create your views here.
def paginaInicio(request):
    return render(request, 'index.html', {})


def contacto(request):
 return render(request, 'contacto.html', {})

@login_required
def mostrarRescatados(request): 
    lista = Rescatado.objects.filter(estado="disponible")
    return render(request,'rescatados.html', {'lista':lista})


def mostrarLogin(request):
        return render(request,'intraweb/login.html', {})



def RegistroUsuario(request):
	if request.user.is_authenticated:
		return redirect('')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Cuenta Creada del usuario:  ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registro.html', context)




