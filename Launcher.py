import os

import Tateti
import Ahorcado
import json


def Eleccion(User, eleccion=''):
    if eleccion == '':
        eleccion = input('Ingrese el nombre juego que quiere jugar (tateti o ahorcado, otro para salir)\n').lower()
    else:
        nuevojuego = input('Presione enter para seguir, el nombre del juego u otro para salir\n').lower()
        if nuevojuego != '':
            eleccion = nuevojuego
    if 'tateti' in eleccion:
        User[eleccion]["victorias"] += Tateti.IniciarJuego(User["nombre"])
    elif 'ahorcado' in eleccion:
        User[eleccion]["victorias"] += Ahorcado.Juego()
    else:
        return
    User[eleccion]["jugadas"] += 1
    MostrarStats(User)
    GuardarDatos(User)
    Eleccion(User, eleccion)


def GuardarDatos(User, Lista=None):
    if not Lista:
        Lista = ListaUsuarios
    for i in range(len(Lista)):
        if Lista[i]["nombre"] == User["nombre"]:
            Lista[i] = User
            f = open("Usuarios.json", 'w')
            stringlista = json.dumps(Lista)
            f.write(stringlista)
            f.close()
            break


def MostrarLog(datos):
    print(f'Logueado como: {datos["nombre"]}\n')
    MostrarStats(datos)


def MostrarStats(datos):
    print(f'Estadisticas:\n'
          f'Ahorcado:\n'
          f'\tJugadas:{datos["ahorcado"]["jugadas"]}\n'
          f'\tVictorias:{datos["ahorcado"]["victorias"]}\n'
          f'Tateti:\n'
          f'\tJugadas:{datos["tateti"]["jugadas"]}\n'
          f'\tVictorias:{datos["tateti"]["victorias"]}')


def CargarDatos():
    if os.path.isfile("Usuarios.json"):
        f = open("Usuarios.json", )
    else:
        f = open("Usuarios.json", "wr")
        f.write('[]')
    Usuarios = json.load(f)
    return Usuarios


def SeleccionarUsuario():
    eleccion = input('Ingrese el nombre de usuario\n').lower()
    for i in ListaUsuarios:
        if i["nombre"] == eleccion:
            return i
    print('No se encontró el usuario')
    return SeleccionarUsuario()


def CrearUsuario(Usuarios):
    nombre = input('Cree un nombre de usuario\n').lower()
    datos = {"nombre": nombre, "ahorcado": {"jugadas": 0, "victorias": 0}, "tateti": {"jugadas": 0, "victorias": 0}}
    Usuarios.append(datos)
    GuardarDatos(datos, Usuarios)
    return datos


def Informacion():
    integrantes = {"Manuel Buslón": 'manuelbuslon22@gmail.com', "Sofia Sanabria": 'sofia.sanabria@correo.ucu.edu.uy'}
    autores = []
    for i in integrantes.keys():
        autores.append(f'Nombre: {i} - Contacto: {integrantes[i]}')
    print('-'*len(max(autores, key=len)))
    print('Autores:')
    print('\n'.join(autores))
    print('-' * len(max(autores, key=len)))
    print('Por dudas o consultas consultas comuniquese a alguno de los correos anteriores\n')


ListaUsuarios = CargarDatos()
Ahorcado.cargar_palabras()
print('Bienvenid@ a el menú de juegos')
if not ListaUsuarios:
    UsuarioActual = CrearUsuario(ListaUsuarios)
else:
    while True:
        opcion = input('Desea loguarse (l) o crear usuario (c)?\n').lower()
        if opcion == 'l':
            UsuarioActual = SeleccionarUsuario()
            break
        elif opcion == 'c':
            UsuarioActual = CrearUsuario(ListaUsuarios)
            break
        else:
            print('Ingrese una opción valida')
MostrarLog(UsuarioActual)
x = input('¿Desea ver informacion del programa?: ').lower()
if 'si' in x:
    Informacion()
Eleccion(UsuarioActual, '')
