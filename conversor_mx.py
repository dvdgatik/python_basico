pesos = input('¿Cuantos pesos mexicanos tienes?: ')
pesos = float(pesos)
valor_pesos = 20
dolar = pesos / valor_pesos
dolar = round(dolar,2)
dolar = str(dolar)
print('Tu tienes: $' + dolar + ' dolares' )
dolares = input('¿Cuantos dolares tienes?: ')
dolares = float(dolares)
peso = dolares * valor_pesos
peso = round(peso,2)
peso = str(peso)
print('Tu tienes: $' + peso + ' mxn')





