from django import forms

class ServicioForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()

class MascotaForm(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    edad = forms.IntegerField()

class MedicamentoForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()

class Filtro(forms.Form):
    nombre = forms.CharField()