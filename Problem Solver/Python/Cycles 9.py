# número factorial
# ejemplo: 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6
# 8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 = 40320

n = int(input('Ingrese un número: '))
if n <= 0:
    print('Ingrese un número postivo: ')
else:
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    print(f'El factorial de {n} es {factorial}')


