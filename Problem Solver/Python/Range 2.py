#mayor que el anterior

valor = int(input('¿Cuántos valores va a introducir?\n '))
if valor < 1:
    print('error')
else:
    primero = int(input('Escriba un número: '))
    for i in range(valor - 1):
        numero = int(input(f'Escriba un número mayor que {primero}: '))
        if numero <= primero:
            print(f'{numero} no es mayor que {primero}')
        primero = numero
        print('Gracias por su colaboración.')
