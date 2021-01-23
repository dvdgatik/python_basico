# pesos = input('¿Cuantos Pesos Colombianos tienes?:')
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2) 
# dolares = str(dolares)
# print('Tienes $' + dolares + ' dolares')

## Convertir de pesos colombianos, argentinos o mexicanos a dolares

menu = '''
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opcion: '''

opcion = input(menu)

if opcion == '1':
	pesos = input('¿Cuantos Pesos Colombianos tienes?: ')
	pesos = float(pesos)
	valor_dolar = 3875
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2) 
	dolares = str(dolares)
	print('Tienes $' + dolares + ' dolares')
elif opcion == '2':
	pesos = input('¿Cuantos Pesos argentinos tienes?: ')
	pesos = float(pesos)
	valor_dolar = 65
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2) 
	dolares = str(dolares)
	print('Tienes $' + dolares + ' dolares')
elif opcion == '3':
	pesos = input('¿Cuantos Pesos mexicanos tienes?: ')
	pesos = float(pesos)
	valor_dolar = 24
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2) 
	dolares = str(dolares)
	print('Tienes $' + dolares + ' dolares')
else:
	print('Ingresa una opcion correcta por favor')



