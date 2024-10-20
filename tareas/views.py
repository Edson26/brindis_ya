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

# ----- LISTADO --------

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

# ----- GESTIONAR --------

#TRABAJDOR
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
def actualizarTrabajador(request, id):
    if request.method == 'GET':
        trabajador = get_object_or_404(Trabajador, id=id)
        form = FormTrabajador(instance=trabajador)
        return r(request, 'actualizarTrabajador.html', {'trabajador': trabajador, 'formularioTrabajador': form})
    else:
        try:
            trabajador = get_object_or_404(Trabajador, id=id)
            form = FormTrabajador(request.POST, instance=trabajador)
            form.save()
            return redirect('listaTrabajador')
        except ValueError:
            return r(request, 'trabajadores.html', {'trabajador': trabajador, 'formularioTrabajador': form, 'error': 'Error al actualizar trabajador.'})
@login_required
def eliminarTrabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    trabajador.delete()
    return redirect('listaTrabajador')

#INGREDIENTE
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
def actualizarIngrediente(request, id):
    if request.method == 'GET':
        ingrediente = get_object_or_404(Ingrediente, id=id)
        form = FormIngrediente(instance=ingrediente)
        return r(request, 'actualizarIngrediente.html', {'ingrediente': ingrediente, 'formIngrediente': form})
    else:
        try:
            ingrediente = get_object_or_404(Ingrediente, id=id)
            form = FormIngrediente(request.POST, instance=ingrediente)
            form.save()
            return redirect('listaIngredientes')
        except ValueError:
            return r(request, 'ingredientes.html', {'ingrediente': ingrediente, 'formIngrediente': form, 'error': 'Error al actualizar ingrediente.'})
@login_required
def eliminarIngrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    ingrediente.delete()
    return redirect('listaIngredientes')

#RECETA
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
def actualizarReceta(request, id):
    if request.method == 'GET':
        receta = get_object_or_404(Receta, id=id)
        form = FormReceta(instance=receta)
        return r(request, 'actualizarReceta.html', {'receta': receta, 'formReceta': form})
    else:
        try:
            receta = get_object_or_404(Receta, id=id)
            form = FormReceta(request.POST, instance=receta)
            form.save()
            return redirect('listaRecetas')
        except ValueError:
            return r(request, 'recetas.html', {'recetas': recetas, 'formReceta': form, 'error': 'Error al actualizar recetas.'})
@login_required
def eliminarReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect('listaRecetas')

#COCTEL
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
@login_required
def actualizarCoctel(request, id):
    if request.method == 'GET':
        coctel = get_object_or_404(Coctel, id=id)
        form = FormCoctel(instance=coctel)
        return r(request, 'actualizarCoctel.html', {'coctel': coctel, 'formCoctel': form})
    else:
        try:
            coctel = get_object_or_404(Coctel, id=id)
            form = FormCoctel(request.POST, instance=coctel)
            form.save()
            return redirect('cocteles')
        except ValueError:
            return r(request, 'cocteles.html', {'cocteles': cocteles, 'formCoctel': form, 'error': 'Error al actualizar coctel.'})
@login_required
def eliminarCoctel(request, id):
    coctel = get_object_or_404(Coctel, id=id)
    coctel.delete()
    return redirect('cocteles')
