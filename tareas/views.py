from django.shortcuts import render as r, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from tareas.forms import FormTrabajador, FormIngrediente, FormReceta, FormCoctel
from .models import Receta, Trabajador, Ingrediente, Coctel


# Funciones de ingreso usuarios

def home(request):
    return r(request, 'index.html')

def singup(request):

    if request.method == 'GET':
        return r(request, 'singup.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('base')
            except:
                return r(request, 'singup.html',{
                'form': UserCreationForm,
                'error': 'Usuario ya existe'
                })
        return r(request, 'singup.html',{
            'form': UserCreationForm,
            'error': 'La contraseña no coincide'
        })

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('home')

def iniciarSesion(request):
    if request.method == 'GET':
        return r(request,'login.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return r(request,'login.html',{
            'form': AuthenticationForm,
            'error':'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('base')

# CRUD Admin

@login_required
def base(request):
    return r(request, 'base.html')

@login_required
def listaTrabajador(request):
    trabajador = Trabajador.objects.all()
    data = {'trabajadores': trabajador}
    return r(request, 'trabajadores.html',data)

@login_required
def listaRecetas(request):
    receta = Receta.objects.all()
    data = {'recetas': receta}
    return r(request, 'recetas.html',data)

@login_required
def listaIngredientes(request):
    ingrediente = Ingrediente.objects.all()
    data = {'ingredientes': ingrediente}
    return r(request, 'ingredientes.html',data)

@login_required
def listaCoctel(request):
    coctel = Coctel.objects.all()
    data = {'cocteles': coctel}
    return r(request, 'cocteles.html', data) 

@login_required
def actualizarTrabajador(request, id):
    if request.method == 'GET':
        trabajador = get_object_or_404(Trabajador, id=id)
        form = FormTrabajador(instance=trabajador)
        return r(request, 'agregarTrabajador.html', {'trabajador': trabajador, 'form': form})
    else:
        try:
            trabajador = get_object_or_404(Trabajador, id=id)
            form = FormTrabajador(request.POST, instance=trabajador)
            form.save()
            return redirect('listaTrabajador')
        except ValueError:
            return r(request, 'trabajadores.html', {'trabajador': trabajador, 'form': form, 'error': 'Error al actualizar trabajador.'})

@login_required
def agregarTrabajador(request):
    form = FormTrabajador()
    if request.method == 'POST':
        form = FormTrabajador(request.POST)
        if (form.is_valid()):
            form.save()
        return listaTrabajador(request)
    data = {'form': form}
    return r(request, 'agregarTrabajador.html',data)

@login_required
def eliminarTrabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    trabajador.delete()
    return redirect('listaTrabajador')

@login_required
def agregarReceta(request):
    form = FormReceta()
    if request.method == 'POST':
        form = FormReceta(request.POST)
        if (form.is_valid()):
            form.save()
        return listaRecetas(request)
    data = {'form': form}
    return r(request, 'agregarReceta.html',data)

@login_required
def agregarIngrediente(request):
    form = FormIngrediente()
    if request.method == 'POST':
        form = FormIngrediente(request.POST)
        if (form.is_valid()):
            form.save()
        return listaIngredientes(request)
    data = {'form': form}
    return r(request, 'agregarIngrediente.html',data)

@login_required
def agregarCoctel(request):
    form = FormCoctel()
    if request.method == 'POST':
        form = FormCoctel(request.POST)
        if(form.is_valid()):
            form.save()
        return listaCoctel(request)
    data = {'form': form}
    return r(request, 'agregarCoctel.html', data)

