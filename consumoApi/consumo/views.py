from django.shortcuts import render
from .services import get_data
from .forms import Formulario
import requests
from django.http import HttpResponseRedirect

def hello_user(request):
	context = []

	for data in get_data():
		context.append({
			'id' : data['id'],
        	'monto': data['monto'],
        	'tipo': data['tipo'],
        	'fecha': data['fecha']
    	})
	#print(context)

	return render(request, 'hello_user.html', {"context" : context })

def newMovement(request):
	form = Formulario()
	if request.method == 'POST':
		form = Formulario(request.POST)
		if form.is_valid():
			url = 'http://localhost:8000/api/'
			payload = {
				"tipo": request.POST['tipo'],
				"monto": request.POST['monto'],
				"fecha": request.POST['fecha'],
				"categoria": request.POST['categoria']}

			response = requests.post(url, json = payload)
	return render(request ,'nuevo_registro.html', {'form':form})

def deleteMovement(request, pk):

	url = 'http://localhost:8000/api/%s'%pk
	print(url)
	response = requests.delete(url)

	print(response.status_code)

	if response.status_code == 204:
		print("elemento borrado")

	return HttpResponseRedirect('/')

def updateMovement(request, pk):
	pkInt = int(pk)
	print(type(pkInt))

	for data in get_data():
		print(type(data['id']))
		if data['id'] == pkInt:
			print('Si entra!!!!!!!!!!!!!!!!!')
			obj = data


	if request.method == 'GET':
		form = Formulario(instance=obj)
	else:
		form = Formulario(request.POST, instance=obj)

		if form.is_valid():
			url = 'http://localhost:8000/api/%s'%pk
			payload = {
				"tipo": request.POST['tipo'],
				"monto": request.POST['monto'],
				"fecha": request.POST['fecha'],
				"categoria": request.POST['categoria']}

			response = requests.put(url, json = payload)

			return HttpResponseRedirect('/')

	return render(request ,'nuevo_registro.html', {'form':form})





