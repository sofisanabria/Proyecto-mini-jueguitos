import Tateti
import Ahorcado
import json


def Eleccion(User, eleccion=''):
    if eleccion == '':
        eleccion = input('Ingrese el juego que quiere jugar (tateti o ahorcado, otro para salir)\n').lower()
    else:
        nuevojuego = input('Presione enter para seguir o el nombre del juego\n').lower()
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
    Eleccion(User)


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
    print(f'Logueado como: {datos["nombre"]}')
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
    f = open("Usuarios.json", )
    Usuarios = json.load(f)
    if not Usuarios:
        CrearUsuario(Usuarios)
    return Usuarios


def SeleccionarUsuario():
    eleccion = input('Ingrese el nombre de usuario\n').lower()
    for i in ListaUsuarios:
        if i["nombre"] == eleccion:
            return i
    return SeleccionarUsuario()


def CrearUsuario(Usuarios):
    nombre = input('Ingrese el nombre de usuario\n').lower()
    datos = {"nombre": nombre, "ahorcado": {"jugadas": 0, "victorias": 0}, "tateti": {"jugadas": 0, "victorias": 0}}
    Usuarios.append(datos)
    GuardarDatos(datos, Usuarios)
    return datos


ListaUsuarios = CargarDatos()
Ahorcado.cargar_palabras()
opcion = input('Desea loguarse (l) o crear usuario (c)?\n').lower()
if opcion == 'l':
    UsuarioActual = SeleccionarUsuario()
else:
    UsuarioActual = CrearUsuario(ListaUsuarios)
MostrarLog(UsuarioActual)
Eleccion(UsuarioActual)
