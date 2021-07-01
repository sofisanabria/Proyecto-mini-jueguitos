import os


def crear():
    tabler = {}
    for i in range(9):
        tabler.update({f'{chr(ord("A") + i // 3)}{(i % 3) + 1}': ' '})
    return tabler


def Imprimir(tablero):
    os.system('cls')
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
    entrada = input('¿Dónde quiere colocar su ficha?\n')
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
        vertical = tablero[f'{i}1'] == tablero[f'{i}2'] == tablero[f'{i}3']
        if vertical:
            if tablero[f'{i}1'] != ' ':
                return tablero[f'{i}1']
    for i in [1, 2, 3]:
        horizontal = tablero[f'A{i}'] == tablero[f'B{i}'] == tablero[f'C{i}']
        if horizontal:
            if tablero[f'A{i}'] != ' ':
                return tablero[f'A{i}']
    diagonal1 = tablero['A1'] == tablero['B2'] == tablero['C3']
    if diagonal1:
        if tablero[f'A1'] != ' ':
            return tablero[f'A1']
    diagonal2 = tablero['A3'] == tablero['B2'] == tablero['C1']
    if diagonal2:
        if tablero[f'A3'] != ' ':
            return tablero[f'A3']
    if ' ' not in list(tablero.values()):
        return 'empate'
    return ' '


def Resultado(resultados):
    print(f'El ganador es {resultados}')
    repetir = input('Desea jugar denuevo? ("si" para continuar)\n')
    if repetir.lower() == 'si':
        IniciarJuego()


def IniciarJuego():
    tablero = crear()
    fichas = list(input('Ingrese las fichas juntas\n'))
    turno = fichas[0]
    siguiente = fichas[1]
    seguir = True
    while seguir:
        Imprimir(tablero)
        turno, siguiente = Preguntar(tablero, turno, siguiente)
        res = Ganar(tablero)
        if res in [fichas[0], fichas[1], 'empate']:
            seguir = False
    Imprimir(tablero)
    Resultado(res)


IniciarJuego()
