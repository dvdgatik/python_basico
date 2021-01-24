# Siempre dejar dos lineas entre cada funcion
def palindromo(palabra):
	palabra = palabra.replace(' ','') # reemplazar espacions por una cadena vacia
	palabra = palabra.lower() #convertir a minusculas
	palabra_invertida = palabra[::-1]
	if palabra == palabra_invertida:
		return True
	else:
		return False

	

def run():
	palabra = input('Ingresa una palabra o frase: ')
	es_palindromo = palindromo(palabra)
	if es_palindromo == True:
		print('Es palindromo')
	else:
		print('No es palindromo')


if __name__ == '__main__':  ##Esta linea es el punto de entrada de un programa de python
	run()