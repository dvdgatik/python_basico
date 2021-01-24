# pesos = input('¿Cuantos Pesos Colombianos tienes?:')
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2) 
# dolares = str(dolares)
# print('Tienes $' + dolares + ' dolares')

## Convertir de pesos colombianos, argentinos o mexicanos a dolares



#Siempre hay que tratar de poner las funciones 
#en el nivel superior arriba de todo

def conversor(tipo_pesos, valor_dolar):
	pesos = input('¿Cuantos Pesos '+ tipo_pesos +' tienes?: ')
	pesos = float(pesos)
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2) 
	dolares = str(dolares)
	print('Tienes $' + dolares + ' dolares')


menu = '''
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opcion: '''




opcion = input(menu)

if opcion == '1':
	conversor('colombianos', 3875)
elif opcion == '2':
	conversor('argentinos', 65)
elif opcion == '3':
	conversor('mexicanos', 24)
else:
	print('Ingresa una opcion correcta por favor')




