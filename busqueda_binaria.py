objetivo = int(input('Escoge un numero: '))
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

#Comparado con la enumeración exhaustiva y la aproximacion con la busqueda binaria tenemos pocos pasos 