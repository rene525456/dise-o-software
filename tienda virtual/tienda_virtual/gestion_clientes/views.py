from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from modelo.models import Cliente
from .forms import ClienteFormulario
from django.contrib.auth.models import User, Group

# Create your views here.
def index(request):
    #listaCliente = Cliente.objects.all().order_by('apellidos')
    #return render(request,'clientes/principal.html', locals())
    return render(request,'clientes/principal.html')
    

def guardar(request):
    
    """
    
    formulario_cliente = ClienteFormulario(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid() and formulario_cuenta.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.genero = datos_cliente.get('genero')
            cliente.estadoCivil = datos_cliente.get('estadoCivil')
            cliente.correo = datos_cliente.get('correo')
            cliente.telefono = datos_cliente.get('telefono')
            cliente.celular = datos_cliente.get('celular')
            cliente.direccion = datos_cliente.get('direccion')
            cliente.save()
            
            return redirect(index)
    return render(request, 'clientes/formulario_crear.html', locals())
    """