import random  #importar un modulo

def run():
	#numero aleatorio entre uno y cien
	numero_aleatorio = random.randint(1,100) #con el punto accedemos a las funciones de un determinado modulo
	numero_elegido = int(input('Elige un numero del 1 al 100: '))
	while numero_elegido != numero_aleatorio:
		if numero_elegido < numero_aleatorio:
			print('Busca un numero mas grande')
		else:
			print('Busca un numero mas pequeño')
		numero_elegido = int(input('Elige otro numero del 1 al 100: '))


	print('¡Ganaste! el numero era el: ' + str(numero_aleatorio))



if __name__ == '__main__':
	run()