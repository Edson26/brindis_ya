"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('singup/', views.singup, name='singup'),
    path('logout/', views.cerrarSesion, name='cerrarSesion'),
    path('login/', views.iniciarSesion, name='login'),
    path('base/', views.base, name='base'),
    path('trabajadores/', views.listaTrabajador, name='listaTrabajador'),
    path('recetas/', views.listaRecetas, name='listaRecetas'),
    path('ingredientes/', views.listaIngredientes, name='listaIngredientes'),
    path('cocteles/', views.listaCoctel, name='cocteles'),
    
    path('agregartrabajador/', views.agregarTrabajador, name='agregarTrabajador'),
    path('agregarreceta/', views.agregarReceta, name='agregarReceta'),
    path('agregaringrediente/', views.agregarIngrediente, name='agregarIngrediente'),
    path('agregarcoctel/', views.agregarCoctel, name='agregarCoctel'),
    
    path('actualizarTrabajador/<int:id>', views.actualizarTrabajador, name='actualizarTrabajador'),
    path('eliminarTrabajador/<int:id>', views.eliminarTrabajador, name='eliminarTrabajador'),
    
    path('actualizarIngrediente/<int:id>', views.actualizarIngrediente, name='actualizarIngrediente'),
    path('eliminarIngrediente/<int:id>', views.eliminarIngrediente, name='eliminarIngrediente'),
    
    path('actualizarCoctel/<int:id>', views.actualizarCoctel, name='actualizarCoctel'),
    path('eliminarCoctel/<int:id>', views.eliminarCoctel, name='eliminarCoctel'),
    
    path('actualizarReceta/<int:id>', views.actualizarReceta, name='actualizarReceta'),
    path('eliminarReceta/<int:id>', views.eliminarReceta, name='eliminarReceta'),
]
