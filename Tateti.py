import os
import random


def crear():
    tabler = {}
    for i in range(9):
        tabler.update({f'{chr(ord("A") + i // 3)}{(i % 3) + 1}': ' '})
    return tabler


def Imprimir(tablero):
    tablerito = '    A   B   C\n' \
                '  ╔═══╦═══╦═══╗\n' \
                '1 ║ {} ║ {} ║ {} ║\n' \
                '  ╠═══╬═══╬═══╣\n' \
                '2 ║ {} ║ {} ║ {} ║\n' \
                '  ╠═══╬═══╬═══╣\n' \
                '3 ║ {} ║ {} ║ {} ║\n' \
                '  ╚═══╩═══╩═══╝\n'.format(tablero['A1'], tablero['B1'], tablero['C1'],
                                           tablero['A2'], tablero['B2'], tablero['C2'],
                                           tablero['A3'], tablero['B3'], tablero['C3'])
    print(tablerito)


def Preguntar(tablero, turno, siguiente):
    entrada = ''.join(sorted(input('¿Dónde quiere colocar su ficha?\n').upper(), reverse = True))
    if entrada in list(tablero.keys()):
        if tablero[entrada] == ' ':
            tablero[entrada] = turno
            return siguiente, turno
        else:
            print('Ya hay una ficha en ese lugar')
    else:
        print('Ese lugar no existe')
    return Preguntar(tablero, turno, siguiente)


def Ganar(tablero):
    for i in ['A', 'B', 'C']:
        if tablero[f'{i}1'] == tablero[f'{i}2'] == tablero[f'{i}3'] != ' ':
            return tablero[f'{i}1']
    for i in [1, 2, 3]:
        if tablero[f'A{i}'] == tablero[f'B{i}'] == tablero[f'C{i}'] != ' ':
            return tablero[f'A{i}']
    if tablero['A1'] == tablero['B2'] == tablero['C3'] != ' ':
        return tablero[f'A1']
    if tablero['A3'] == tablero['B2'] == tablero['C1'] != ' ':
        return tablero[f'A3']
    if ' ' not in list(tablero.values()):
        return 'empate'
    return ' '


def Resultado(resultados, datos):
    if resultados == 'empate':
        print('El resultado es empate')
    else:
        print(f'El ganador es {datos[resultados]}')
        if datos[resultados] != 'el invitado':
            return 1
    return 0


def IniciarJuego(nombre, victorias=0):
    tablero = crear()
    fichas = ['', '']
    while len(fichas[0]) != 1 or len(fichas[1]) != 1:
        fichas = input(f'Ingrese la ficha de {nombre} seguida de la ficha del invitado\n').split()
        if len(fichas) != 2:
            fichas = input(f'Ingrese la ficha de {nombre} seguida de la ficha del invitado\n').split()
    datos = {fichas[0]: nombre, fichas[1]: 'el invitado'}
    primero = random.randint(0, 1)
    print(f'Primero le toca a {"el invitado" if primero else nombre}')
    turno = fichas[primero]
    siguiente = fichas[1-primero]
    seguir = True
    while seguir:
        Imprimir(tablero)
        turno, siguiente = Preguntar(tablero, turno, siguiente)
        res = Ganar(tablero)
        if res in [fichas[0], fichas[1], 'empate']:
            seguir = False
    Imprimir(tablero)
    return Resultado(res, datos)
