from django.shortcuts import render, redirect
from App.models import Usuario, Mascota, Medicamento
# Create your views here.

def show_html(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def crear_usuario(request):
    return redirect("/app/usuarios/")

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        "usuarios": usuarios
    }

    return render(request, 'App/usuarios.html', contexto)

def filtrar_usuarios(request):
    ...

def crear_mascota(request):
    return redirect("/app/mascotas/")

def mostrar_mascotas(request):
    mascotas = Mascota.objects.all()
    contexto = {
        "mascotas": mascotas
    }

    return render(request, 'App/mascotas.html', contexto)

def filtrar_mascotas(request):
    ...

def crear_medicamento(request):
    return redirect("/app/medicamentos/")

def mostrar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    contexto = {
        "medicamentos": medicamentos
    }

    return render(request, 'App/medicamentos.html', contexto)

def filtrar_medicamentos(request):
    ...