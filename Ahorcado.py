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


def Modo():
    x = input('Elija el modo que quiere jugar:  Facil   Medio   Dificil\n')
    if x in Palabras.keys():
        PalabraSecreta = Palabras[x][random.randint(0, len(Palabras[x]) - 1)]
        print(f'La palabra tiene {len(PalabraSecreta)} letras')
        #print(f'Es: {PalabraSecreta}')
    return PalabraSecreta


def Letras(palabra):
    letritas = {}
    for i in palabra:
        letritas[i] = 1
    return list(letritas.keys())


def Partes(intento):
    cuerpo = ['0', '|', '/', '\\', '|', '/', '\\']
    actual = ['', '', ' ', '', '', '', '']
    for i in range(intento - 1):
        actual[i] = cuerpo[i]
    horca = f'╔═════╗' \
            f'\n║     {actual[0]}' \
            f'\n║    {actual[2]}{actual[1]}{actual[3]}' \
            f'\n║     {actual[4]}' \
            f'\n║    {actual[5]} {actual[6]}'
    return horca


def dibujar(Palabra, Letrass, Aciertos, intento):
    palabra_escondida = Palabra
    for i in Letrass:
        if i not in Aciertos:
            palabra_escondida = palabra_escondida.replace(i, '_')
    palabra_escondida = ' '.join(list(palabra_escondida))
    horca = Partes(intento)
    horca += f'\n╨\t\t{palabra_escondida}'
    print(horca)


def Juego():
    PalabraSecret = Modo()
    letras = Letras(PalabraSecret)
    fallos = 7
    intentos = 1
    aciertos = []
    while intentos <= fallos:
        dibujar(PalabraSecret, letras, aciertos, intentos)
        if sorted(letras) == sorted(aciertos):
            print(f'Ganaste, te tomó {intentos} intento')
            break
        entrada = input('Ingrese una letra o escriba "arriesgar": ')
        if entrada == 'arriesgar':
            entrada = input('Ingrese la palabra: ')
            if entrada == PalabraSecret:
                aciertos = letras
                break
            else:
                break
        if entrada in letras and entrada not in aciertos:
            aciertos.append(entrada)
            continue
        intentos += 1

    dibujar(PalabraSecret, letras, aciertos, intentos)
    if intentos <= fallos:
        print(f'Ganaste, te tomó {intentos} intento')
    else:
        print('Perdiste')
    print(f'La palabra era {PalabraSecret}')


cargar_palabras()
while True:
    Juego()
