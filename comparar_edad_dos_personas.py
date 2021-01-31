def main():
	u1_name = input('Ingresa el nombre del usuario 1: ')
	u1_age = int(input('Ingresa la edad del usuario 1: '))
	u2_name = input('Ingresa el nombre del usuario 2: ')
	u2_age = int(input('Ingresa la edad del usuario 2: '))

	if u1_age > u2_age:
		print(f'{u1_name} es mayor que {u2_name}')
	elif u1_age < u2_age:
		print(f'{u2_name} es mayor que {u1_name}')
	else:
		print(f'{u1_name} y {u2_name} tienen la misma edad')



if __name__ == '__main__':
	main()