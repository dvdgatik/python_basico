#Hacer un Programa en python que te siga si un numero es primo o no lo es

def es_primo(numero):
	contador = 0
	# numero+1 para asegurar el intervalo
	for i in range(1,numero+1):
		print(i)
		if  i == 1 or i == numero: #comprobar si es igual a uno o a si mismo 
			continue
		if numero % i == 0: #compruebas si es entero y si no es un numero que no sea 1 y el mismo
			contador += 1
	if contador == 0:
		return True
	else:
		return False

	

def run():
	numero = int(input('Escribe un numero: '))
	if es_primo(numero):
		print('Es primo')
	else:
		print('No es primo') 



if __name__ == '__main__':
	run()