import random


def adivina_el_numero():
    print('======================================')
    print(' ¡Bienvenido(a) al Juego! ')
    print('======================================')
    print('')

    num= int(input('Escribe el numero que lanzara la computadora del 1 al 10\n'))

    numero_aleatorio = random.randint(1,10)

    if num == numero_aleatorio:
        print(f'Acertaste en el numero Tu: {num} -- Computador: {numero_aleatorio}')
    else:
        print(f'No le atinaste tu numero : {num} -- computadora : {numero_aleatorio}')



adivina_el_numero()