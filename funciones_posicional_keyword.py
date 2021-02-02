def nombre_completo(nombre, apellido, inverso=False):
	if inverso:
		return print(f'{apellido} {nombre}')
	else:
		return print(f'{nombre} {apellido}')

nombre_completo('David', 'Aroesti')
nombre_completo('David', 'Aroesti', inverso=True)
nombre_completo(apellido='Aroesti', nombre='David')
