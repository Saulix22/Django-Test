from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Material
from .forms import MaterialForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def base(request):
    return render(request, 'base.html')

def materiales(request):
    materiales = Material.objects.all()
    return render(request, 'materiales/index.html', {'materiales': materiales})

def crear(request):
    formulario = MaterialForm(request.POST or None, request.FILES or None)
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
