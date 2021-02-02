def enumeracion(objetivo):
	print('Enumeracion Exhaustiva')
	respuesta = 0

	while respuesta**2 < objetivo:
		print(respuesta)
		respuesta += 1


	if (respuesta)**2 == (objetivo):
		print(f'La raiz cuadrada de {objetivo} es {respuesta}')
	else:
		print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aprox(objetivo):
	print('Aproximación')
	epsilon = 0.0001 
	paso = epsilon**2 
	respuesta =  0.0
	while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
		respuesta += paso

	if abs(respuesta**2 - objetivo) >= epsilon:
		print(f'No se encontro la raiz cuadrada de {objetivo}')
	else:
		print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
	print('Búsqueda Binaria')
	epsilon = 0.0001
	bajo = 0.0 #limite inferior
	alto = max(1.0, objetivo) #limite superior # max: regresa el valor mas alto entre dos valores
	#con max garantizamos que no tenemos valores negativos

	respuesta = (alto + bajo) / 2 # dividir entre dos el alto y bajo
	while abs(respuesta**2 - objetivo) >= epsilon:
		print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
		if respuesta**2 < objetivo:
			bajo = respuesta
		else:
			alto = respuesta

		respuesta = (alto + bajo) / 2
	print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
	opcion = int(input('''
	Elige una solucion para calcular Raíz Cuadrada
	Opciones:
	1. Enumeracion Exhaustiva
	2. Aproximación
	3. Búsqueda Binaria
	'''))
	objetivo = abs(int(input('Escoge un numero: ')))
	if opcion == 1:
		enumeracion(objetivo)
	elif opcion == 2:
		aprox(objetivo)
	elif opcion == 3:
		busqueda_binaria(objetivo)
	else:
		print('Ingresa una opcion valida')




if __name__ == '__main__':
	run()	



