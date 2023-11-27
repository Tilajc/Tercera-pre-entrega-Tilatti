"""
URL configuration for ProyectoCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from App.views import show_html, mostrar_servicios, mostrar_mascotas, mostrar_medicamentos, agregar_servicio, agregar_mascota, agregar_medicamento, filtrar_servicios, filtrar_mascotas, filtrar_medicamentos

urlpatterns = [
    path('show/', show_html),
    path('servicios/', mostrar_servicios),
    path('mascotas/', mostrar_mascotas),
    path('medicamentos/', mostrar_medicamentos),
    path('agregar_servicio/', agregar_servicio),
    path('agregar_mascota/', agregar_mascota),
    path('agregar_medicamento/', agregar_medicamento),
    path('filtrar_servicios/', filtrar_servicios),
    path('filtrar_mascotas/', filtrar_mascotas),
    path('filtrar_medicamentos/', filtrar_medicamentos)
]
