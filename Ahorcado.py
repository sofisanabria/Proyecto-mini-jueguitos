import random

Palabras = {}


def cargar_palabras():
    file = open("Palabras.txt", "r")
    guardar = ''
    for line in file:
        li = line.strip()
        if '-' in li:
            guardar = li[1:]
            if guardar not in Palabras.keys():
                Palabras[guardar] = []
            continue
        if li == '':
            continue
        Palabras[guardar].append(li.lower())
    file.close()


def Jugar():
    x = input('Elija el modo que quiere jugar:  Facil   Medio   Dificil\n')
    if x in Palabras.keys():
        PalabraSecreta = Palabras[x][random.randint(0, len(Palabras[x]) - 1)]
        print(f'La palabra tiene {len(PalabraSecreta)} letras')
        print(f'Es: {PalabraSecreta}')
    return PalabraSecreta


def Letras(palabra):
    letritas = {}
    for i in palabra:
        letritas[i] = 1
    return list(letritas.keys())


def dibujar(Palabra, Letrass, Aciertos):
    palabra_escondida = Palabra
    for i in Letrass:
        if i not in Aciertos:
            palabra_escondida = palabra_escondida.replace(i, '_')
    palabra_escondida = ' '.join(list(palabra_escondida))
    print(f'╔═════╗'
          f'\n║'
          f'\n║'
          f'\n║'
          f'\n╨\t\t{palabra_escondida}'
          )


r"""
-----
|   0
|  /|\
|   |
|  / \      --o--a-a--o-
"""

cargar_palabras()
PalabraSecret = Jugar()
letras = Letras(PalabraSecret)
fallos = 7
intentos = 1
aciertos = []
while intentos <= fallos:
    dibujar(PalabraSecret, letras, aciertos)
    if sorted(letras) == sorted(aciertos):
        print(f'Ganaste, te tomó {intentos} intento')
        break
    entrada = input('Ingrese una letra o escriba "arriesgar": ')
    if entrada == 'arriesgar':
        entrada = input('Ingrese la palabra: ')
        if entrada == PalabraSecret:
            print(f'Ganaste, te tomó {intentos} intento')
            break
    if entrada in letras and entrada not in aciertos:
        aciertos.append(entrada)
        continue
    intentos += 1
