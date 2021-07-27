"""
Trabajo en progreso de modelos nesesarios
"""
import datetime as dt
from bottle import response, request


"""
    Funcion para generar una nueva nota
    recibe los argumentos

     - nombre, una cadena de texto que corresponda al nombre de la nota.
     - categoria, una cadena de texto que carga el mensaje a estructurar.
     - contenido, una cadena de texto en la cual se alamacena todo el texto que compondra el cuerpo de la nota
     - fecha, una cadena de texto que represente la fecha en formato iso.
     - id, es una cadena de texto compuesta por el nombre de la nota y la fecha de creacion

    La fecha de creacion de agregara automaticamente, al igual que el identificador correspondiente.
    El unico campo que sera necesario de llenar al momento de crear una nota es el titulo (se pueden dejar en blanco los campos de categoria, y contenido.).

    Esta funcion regresara un diccionario con 5
    llaves, 'nombre', 'categoria' y 'contenido', 'fecha', 'id'.

    ### Correcto
    >>> estructurar_mensaje('Avance de proyecto', 'Escuela', 'se realizaron avances los caules se exponeran a continuacion....')
    {'nombre': 'Avance de proyecto', 'categoria': 'Escuela', 'contenido': '', 'fecha':'2021-05-01T20:23:22', 'id':'Avance de proyecto-2021-05-01T20:23:22' }

    ### Incorrecto
    >>>estructurar_mensaje('', 'Escuela', 'se realizaron avances los caules se exponeran a continuacion....')
    Traceback
     ...
    Exception: Nombre invalido.
"""
def creador_nota(nombre, categoria, contenido):

    try:
        fecha = dt.datetime.fromisoformat(fecha)
        id = nombre + '-' + fecha
    except:
        raise Exception("Nombre no valido.")
    return {
        "name": name,
        "categoria": category,
        "contenido": content,
        "fecha": date.isoformat(),
        "id": id
        }




"""
    Funcion para generar una nueva categoria
    recibe los argumentos

     - nombre, una cadena de texto que corresponda al nombre de la categoria.
     - descripcion, una cadena de texto que contenga informacion adicional para una categoria (campo opcional).

    No se requiere de utilziar una descipcion para la cateroia, este es un campo que puede ir vacio, en cambio es obligatorio
    colocar el nombre de la categoria (este nombre tiene que ser unico)

    Esta funcion regresara un diccionario con 2
    llaves, 'nombre', 'descipcion'.

    ### Correcto
    >>> estructurar_mensaje('Arte', 'En esta categorias encontraras notas relacionadas al arte.')
    {'nombre': 'Arte', 'descripcion': 'En esta categorias encontraras notas relacionadas al arte.'}

    ### Incorrecto
    >>>
    estructurar_mensaje('','En esta categorias encontraras notas relacionadas al arte.')
    o
    este caso, es si ya exsistia una categoria con el mismo
    estructurar_mensaje('Arte','')
    Traceback
     ...
    Exception: Nombre invalido.
"""
def creador_categoria(nombre, descripcion):
    try:
        pass
    except:
        raise Exception("Nombre no valido.")

    return {
        "nombre": nombre,
        "descripcion": descipcion,
        }
