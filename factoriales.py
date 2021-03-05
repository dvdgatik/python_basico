
def factorial(n):
    """Summary
    Calcula el factorial de n
    Args:
        n int > 0
        returns n!
    """
    print(n)
    if n == 1:
    	return 1

    return n * factorial(n - 1)


n = int(input('Escribe un entero: '))

print(factorial(n))