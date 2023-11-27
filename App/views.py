from django.shortcuts import render, redirect
from App.models import Servicio, Mascota, Medicamento
from App.forms import ServicioForm, MascotaForm, MedicamentoForm, Filtro


# Create your views here.

def show_html(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def agregar_servicio(request):
    if request.method == "POST":
        servicio_formulario = ServicioForm(request.POST)
        if servicio_formulario.is_valid():
            informacion = servicio_formulario.cleaned_data
            servicio_agregar = Servicio(nombre = informacion["nombre"], descripcion=informacion["descripcion"],precio=informacion["precio"])
            servicio_agregar.save()

            return redirect("/app/servicios")

    servicio_form = ServicioForm()
    contexto = {
        "form": servicio_form
    }

    return render(request, "App/agregar_servicio.html", contexto)

def mostrar_servicios(request):
    servicios = Servicio.objects.all()
    contexto = {
        "servicios": servicios,
        "form": Filtro()
    }

    return render(request, 'App/servicios.html', contexto)

def filtrar_servicios(request):
    nombre = request.GET["nombre"]
    servicios = Servicio.objects.filter(nombre__icontains=nombre)

    contexto = {
        "servicios": servicios,
        "form": Filtro()
    }

    return render(request, 'app/servicios.html', contexto)

def agregar_mascota(request):

    if request.method == "POST":
        mascota_formulario = MascotaForm(request.POST)

        if mascota_formulario.is_valid():
            informacion = mascota_formulario.cleaned_data
            mascota_agregar = Mascota(nombre=informacion["nombre"], tipo=informacion["tipo"], edad=informacion["edad"])
            mascota_agregar.save()

            return redirect("/app/mascotas")

    mascota_form = MascotaForm()

    contexto = {
        "form": mascota_form
    }

    return render(request, "App/agregar_mascota.html", contexto)

def mostrar_mascotas(request):
    mascotas = Mascota.objects.all()
    contexto = {
        "mascotas": mascotas,
        "form": Filtro()
    }

    return render(request, 'App/mascotas.html', contexto)

def filtrar_mascotas(request):
    nombre = request.GET["nombre"]
    mascotas = Mascota.objects.filter(nombre__icontains=nombre)

    contexto = {
        "mascotas": mascotas,
        "form": Filtro()
    }

    return render(request, 'App/mascotas.html', contexto)

def agregar_medicamento(request):
    if request.method == "POST":
        medicamento_form = MedicamentoForm(request.POST)
        if medicamento_form.is_valid():
            informacion = medicamento_form.cleaned_data
            medicamento_agregar = Medicamento(nombre=informacion["nombre"], precio=informacion["precio"])
            medicamento_agregar.save()

            return redirect("/app/medicamentos")

    medicamento_form = MedicamentoForm()

    contexto = {
        "form": medicamento_form
    }

    return render(request, 'App/agregar_medicamento.html', contexto)

def mostrar_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    contexto = {
        "medicamentos": medicamentos,
        "form": Filtro()
    }

    return render(request, 'App/medicamentos.html', contexto)

def filtrar_medicamentos(request):
    nombre = request.GET["nombre"]
    medicamentos = Medicamento.objects.filter(nombre__icontains=nombre)

    contexto = {
        "medicamentos": medicamentos,
        "form": Filtro()
    }

    return render(request, 'App/medicamentos.html', contexto)