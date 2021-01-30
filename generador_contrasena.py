## el generador de contraseñas es una combinacion de Letras mayus, minus, numeros y simbolos
import random

def generar_contrasena():
	mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	minusculas = ['a','b','c','d','e','f','g']
	simbolos = ['!','#','$','&','/','(',')','_','.','¡']
	numeros = ['1','2','3','4','5','6','7','8','9','0']

	caracteres = mayusculas + minusculas + simbolos + numeros

	contrasena = []

	for i in range(15):
		#choice eligo un caracter alazar de la lista y lo guardo en la variable random
		caracter_random = random.choice(caracteres)
		contrasena.append(caracter_random)

	#join para unir la lista array a una cadena string 
	contrasena = ''.join(contrasena)
	return contrasena




def run():
	contrasena = generar_contrasena()
	print('Tu nueva contraseña es: ' + contrasena)




if __name__ == '__main__':
	run()