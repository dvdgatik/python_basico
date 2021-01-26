def run():
	#imprimir solo los pares
	# for contador in range(1000):
	# 	if contador % 2 != 0:
	# 		continue #lo que esta debajo de continue no se va a ejecutar y pasamos a la siguiente vuelta del ciclo
	# 	print(contador)
	# for i in range(0,10000) :
	# 	print(i)
	# 	if i == 10:
	# 		break #rompe el ciclo y ya no se ejecuta
	# escribir un texto hasta encontrar la letra o y detenerlo
	# texto = input('Escribe un texto')
	# for letra in texto:
	# 	if letra == 'o':
	# 		break
	# 	print(letra)

	# Tambien podemos usar ciclos
	 texto = input('Escribe una palabra u oración: ')
	 letra = 0
	 while len(texto) >= letra:
	 	if len(texto) <= letra:
	 		break # la longitud no esta en el arreglo de la cadena por lo que marca error por eso hay que suar break
	 	print(texto[letra])
	 	letra += 1 





if __name__ == '__main__':
	run() 