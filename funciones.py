# def imprimir_mensaje():
# 	print('Mensaje especial: ')
# 	print('Estoy Aprendiendo a usar funciones')


# imprimir_mensaje() ## invocando una funcion (voy ala definicion de la funcion y ejecuto lo que esta adentro)
# imprimir_mensaje()
# imprimir_mensaje()
# 

#parametros: variables disponibles dentro de las funciones
def conversacion(mensaje): #parametro que recibe la funcion al invocarla
	print('hola')
	print('como estas')
	print(mensaje)
	print('adios')


# opcion = int(input('Elige una opcion (1,2,3): '))
# if opcion == 1:
# 	conversacion('elegiste la opcion 1')
# elif opcion == 2:
# 	conversacion('elegiste la opcion 2')
# elif opcion == 3:
# 	conversacion('elegiste la opcion 3')
# else:
# 	print('Escribe la opcion correcta')

def suma(a, b):
	print('Se suman dos numeros')
	resultado = a + b
	return resultado
	# devuelve el valor para utilizarlo despues
	# la variable resultado va a ser regresada


sumatoria = suma(1,4)
print(sumatoria)


