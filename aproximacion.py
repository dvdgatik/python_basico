objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001 #que tan_ cerca queremos llegar de la respuesta
paso = epsilon**2 #numero mas pequeño 0.01*0.01

respuesta =  0.0

#abs valor absoluto
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: #la segunda iteracion nos protege contra negativos
	#print(abs(respuesta**2 - objetivo), respuesta)
	respuesta += paso
	


if abs(respuesta**2 - objetivo) >= epsilon:
	print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
	print(f'La raiz cuadrada de {objetivo} es {respuesta}')
