import requests
import json

# METODOS GET CON POKEAPI--------------------------------------------------------------------------------------

# url = 'http://pokeapi.co/api/v2/pokemon-form/'

# response = requests.get(url) #Obtener todo
# if response.status_code == 200:

# 	#print(response.content) 

# 	payload = response.json() #obtener todo en formato JSON
# 	nex = payload['next'] #Obtener una llave del objeto JSON
# 	print('Siguente pokemon: ', nex)
# 	results = payload.get('results', []) #Obtener objetos JSON en una llave de otro objeto JSON

# 	lis = []

# 	if results:
# 		for poke in results:
# 			name = poke['name']
# 			lis.append(name)
# 		print(lis)
# 		
# METODO POST --------------------------------------------------------------------------------------------

# url = 'http://httpbin.org/post'
# payload = {'nombre':'santiago','apellido':'tapasco','edad':'20'}

# response = requests.post(url, json = payload)

# if response.status_code == 200:
# 	print(response.content)
# 	----------------------------------------------------------------------------------------------------------
# 	
# 	
# 	
# -------------------------------------PRACTICA METODOS  PARA APP PRESUPUESTO
# 
# 
# 
# 
# METODO GET----------------------------------------------

# url = 'http://localhost:8000/api/'

# response = requests.get(url) #Obtener todo
# if response.status_code == 200:

# 	print(response.content) 

# 	payload = response.json() #obtener todo en formato JSON

# 	position = payload[0] # obtener posicion de la lista

# 	print(position)


# 	lis = []

# 	if payload:
# 		for poke in payload:
# 			fecha = poke['fecha']
# 			lis.append(fecha)
# 		print(lis)

#METODO POST --------------------------------------------
#
# url = 'http://localhost:8000/api/'

# payload = {"tipo": "Ingreso","monto": "222", "fecha": "2020-01-30", "categoria": 1}

# response = requests.post(url, json = payload)

# if response.status_code == 200:
# 	print(response.content)
	
# METODO PUT --------------------------------------------- 

# url = 'http://localhost:8000/api/15'

# payload = {"tipo": "Ingreso","monto": "222", "fecha": "2020-01-30", "categoria": 1}

# response = requests.put(url, json = payload)

# if response.status_code == 200:
# 	print(response.content)

#METODO DELETE ---------------------------------------------
# extend = '16'

# url = 'http://localhost:8000/api/%s'%extend
# print(url)
# response = requests.delete(url)

# print(response.status_code)

# if response.status_code == 204:
# 	print("elemento borrado")
	
	
# 	
# 	------------------------------------------------------------
# 	
url = 'http://localhost:8000/api/'

response = requests.get(url)
if response.status_code == 200:
	payload = response.json()
	lis = []

	if response:
		for data in payload:
			pk = data['id']
			monto = data['monto']
			tipo = data['tipo']
			fecha = data['fecha']
			lis.append({
					'id':pk,
					'monto':monto,
					'tipo': tipo,
					'fecha': fecha
				})
				
		print (lis)
