## Imprimir todas las potencias de dos hasta llegar al mil, hasta millon

## Ciclo While

def run():
	LIMITE = 1000000 # una constante se define con las palabras en Mayusculas
	contador = 0
	potencia_2 = 2**contador #todo numero elevado a la cero es igual a uno
	while potencia_2 < LIMITE:
		print('2 elevado a ' + str(contador)+' es igual a: '+str(potencia_2))
		contador = contador + 1
		potencia_2 = 2**contador


if __name__ == '__main__':
	run()


