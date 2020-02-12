import requests

def get_data():
	url = 'http://localhost:8000/api/'

	response = requests.get(url)
	if response.status_code == 200:
		payload = response.json()
		#print(payload)
		lis = []

		if response:
			for data in payload:
				pkInit = data['id'],
				pk = pkInit[0]
				monto = data['monto']
				tipo = data['tipo']
				fecha = data['fecha']
				lis.append({
						'id' : pk,
						'monto':monto,
						'tipo': tipo,
						'fecha': fecha
					})

		return lis
    