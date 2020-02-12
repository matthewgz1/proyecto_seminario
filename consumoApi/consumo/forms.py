from django import forms

class Formulario(forms.Form):
	tipo = forms.CharField(max_length=100)
	monto =forms.CharField()
	fecha = forms.CharField()
	categoria = forms.IntegerField()
