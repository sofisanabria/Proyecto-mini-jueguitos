import os
import random
Palabras = {}


# Funcion que carga las palabras que se usarán
def cargar_palabras():
    carpeta = 'Palabras/'
    contenido = os.listdir(carpeta)
    for tema in contenido:
        if tema.endswith('.txt'):
            file = open(f'{carpeta}{tema}', "r")
            datos = file.read().replace('\n\n', '\n')
            Palabras[tema.replace('.txt', '')] = datos.split()
            file.close()


# Seleccionamos el modo de juego, que categoria se usará
def Modo():
    modos = list(Palabras.keys())
    modosF = []
    # Cargamos los modos en una lista y solo mostramos los que no esten como --Algo
    for i in modos:
        if '-' in i:
            # Salteamos si es modo secreto
            continue
        else:
            # Le ponemos comillas
            modosF.append(f'"{modos[modos.index(i)]}"')
    cadena_modos = ' '.join(modosF)
    x = input(f'Elija el modo que quiere jugar:  {cadena_modos}\n')
    if x in Palabras.keys():
        PalabraSecreta = random.choice(Palabras[x]).lower()
        print(f'La palabra tiene {len(PalabraSecreta)} letras')
        # print(f'Es: {PalabraSecreta}')
    else:
        return Modo()
    return PalabraSecreta


# Creamos una lista con las letras de la palabra
def Letras(palabra):
    letritas = {}
    for i in palabra:
        # Si son espacios no nos interesa eso
        if i != ' ':
            letritas[i] = 1
    # Devolvemos una lista de las llaves, las letras distintas
    return list(letritas.keys())


# Creamos la horca con las partes del cuerpo
def Partes(intento, errores):
    # Cuerpo entero
    cuerpo = ['0', '|', '/', '\\', '|', '/', '\\']
    actual = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Contamos los fallos y agregamos partes por cada uno
    for i in range(intento - 1):
        actual[i] = cuerpo[i]
    # Se usa string f para armarlo con lo actual
    # Se imprimen tambien los errores
    horca = f'╔═════╗ Letras mal: {", ".join(errores)}' \
            f'\n║     {actual[0]}' \
            f'\n║    {actual[2]}{actual[1]}{actual[3]}' \
            f'\n║     {actual[4]}' \
            f'\n║    {actual[5]} {actual[6]}'
    # Devolvemos la parte de arriba de la horca
    return horca


# Escondemos la palabra
def Esconder(Palabra, Letrass, Aciertos):
    palabra_escondida = Palabra
    # Si es un espacio lo reemplazamos por una barra
    palabra_escondida = palabra_escondida.replace(' ', '/')
    for i in Letrass:
        if i not in Aciertos:
            palabra_escondida = palabra_escondida.replace(i, '_')
    # Añadimos espacios entre cada letra, para que se vea mejor
    palabra_escondida = ' '.join(list(palabra_escondida))
    return palabra_escondida


# Cargamos toda la horca y la imprimimos
def dibujar(Palabra, Letrass, Aciertos, errores, intento):
    palabra_escondida = Esconder(Palabra, Letrass, Aciertos)
    horca = Partes(intento, errores)
    horca += f'\n╨\t\t{palabra_escondida}'
    print(horca)


# Funcion de juego, se repite para cada nueva partida
def Juego():
    PalabraSecret = Modo()  # Seleccionamos la palabra
    letras = Letras(PalabraSecret)  # Cargamos sus letras
    fallos = 7  # Total de fallos permitidos
    intentos = 1
    aciertos = []  # Guardamos las letras que seleccione bien
    errores = []   # Guardamos las letras que ingrese mal
    while intentos <= fallos:
        dibujar(PalabraSecret, letras, aciertos, errores, intentos)
        # Vemos si los aciertos son iguales a las letras, por si ganó
        if sorted(letras) == sorted(aciertos):
            # Usamos el break para salir del while y nos encargamos luego
            break
        # Modo de arriesgar
        entrada = input('Ingrese una letra o escriba "arriesgar": ').lower()
        if entrada == 'arriesgar':
            entrada = input('Ingrese la palabra: ').lower()
            # Si adivino completamos las letras y salimos
            if entrada == PalabraSecret:
                aciertos = letras
                break
            else:
                # Perdio completamente y salimos, quitandole los intentos
                intentos = fallos+1
                break
        # Nos fijamos si la letra que ingreso es una de las que le falta y aun no la adivino
        if entrada in letras:
            if entrada not in aciertos:
                aciertos.append(entrada)
            continue
        # Si no es correcta y es una letra se agrega a errores
        elif len(entrada) == 1:
            if entrada in errores:
                continue
            errores.append(entrada)
        intentos += 1

    dibujar(PalabraSecret, letras, aciertos, errores, intentos)
    devolver = 0
    # Si los intentos no superan los fallos ganó
    if intentos <= fallos:
        print(f'Ganaste, te tomó {intentos} intento')
        devolver = 1
    else:
        print('Perdiste')
    print(f'La palabra era {PalabraSecret}')
    return devolver
