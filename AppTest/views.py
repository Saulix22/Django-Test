from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Material, Solicitud
from .forms import MaterialForm, SolicitudForm
from django.db import IntegrityError

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'paginas/iniciarSesion.html', {
        'form': AuthenticationForm
        })  
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST["password"])
        if user is None:    
            return render(request, 'paginas/iniciarSesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña es incorrecta'
            })  
        else: 
            login(request, user)
            return redirect('inicio')

def registro(request):
    if request.method == 'GET':
        return render(request, 'paginas/registro.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try: 
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'paginas/registro.html', {
                    'form': UserCreationForm, 
                    'error': 'El usuario ya existe'
                })
            
        return render(request, 'paginas/registro.html', {
                'form': UserCreationForm, 
                'error': 'Las contraseñas no coinciden'
            })
    
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def base(request):
    return render(request, 'base.html')

def materiales(request):
    materiales = Material.objects.all()
    return render(request, 'materiales/index.html', {'materiales': materiales})

def crear(request):
    formulario = MaterialForm(request.POST or None, request.FILES or None)
    print(formulario)
    if formulario.is_valid():
        formulario.save()
        return redirect('materiales')
    return render(request, 'materiales/crear.html', {'formulario': formulario})

def editar(request, id):
    material = Material.objects.get(id=id)
    formulario = MaterialForm(request.POST or None, request.FILES or None, instance=material)
    if formulario.is_valid() and  request.POST:
        formulario.save()
        return redirect('materiales')
    return render(request, 'materiales/editar.html', {'formulario': formulario})

def eliminar(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    return redirect('materiales')

def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'solicitudes/inicio.html', {'solicitudes': solicitudes})

def crearSolicitud(request):
    
    if request.method == 'GET':
        return render(request, 'solicitudes/crear.html', {'formulario': SolicitudForm})
    else:
        try:
            formulario = SolicitudForm(request.POST)
            newForm = formulario.save(commit=False)
            newForm.user = request.user
            newForm.save()
            return redirect('solicitudes')
        except ValueError:
            return render(request, 'solicitudes/crear.html', {'formulario': SolicitudForm, 'error': 'Ingresa datos validos'})
            
    
def eliminarSolicitud(request, id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect('solicitudes')