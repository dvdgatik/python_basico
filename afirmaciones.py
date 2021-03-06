# assert <expresion booleana>, <mensaje de error>
# Recibe una lista de palabras y toma la primera letra de cada una  y regresa una lista nueva con estas palabras 
def primera_letra(lista_de_palabras):
	primeras_letras = []

	for palabra in lista_de_palabras:
		try:
			assert type(palabra) == str, f'{palabra} no es str'
			assert len(palabra) > 0, 'No se permiten str vacios'
			primeras_letras.append(palabra[0])
		except AssertionError as e:
			print(e)
	

	return primeras_letras


print(primera_letra(['David',20,'Tomas','']))





