import json
from datetime import datetime
from modules.storage import (
    store_string, store_bytes,
    query_storage, get_storage_file
)


#Crear nota
def create_n(datee=None, name=None, category=None, body=None):
    """
        Funcion para generar una nueva nota
        recibe los argumentos

         - name, una cadena de texto que corresponda al nombre de la nota.
         - category, una cadena de texto que carga el mensaje a estructurar.
         - date, una cadena de texto en la cual se alamacena todo el texto que compondra el cuerpo de la nota
         - fecha, una cadena de texto que represente la fecha en formato iso.
         - id, es una cadena de texto compuesta por el nombre de la nota y la fecha de creacion

        La fecha de creacion de agregara automaticamente, al igual que el identificador correspondiente.
        El unico campo que sera necesario de llenar al momento de crear una nota es el titulo (se pueden dejar en blanco los campos de categoria, y contenido.).

        Esta funcion regresara un diccionario con 5
        llaves, 'nombre', 'categoria' y 'contenido', 'fecha', 'id'.

        ### Correcto
        >>> estructurar_mensaje('Avance de proyecto', 'Escuela', 'se realizaron avances los caules se exponeran a continuacion....')
        {'name': 'Avance de proyecto', 'category': 'Escuela', 'content': '', 'date':'2021-05-01T20:23:22', 'id':'Avance de proyecto-2021-05-01T20:23:22' }

        ### Incorrecto
        >>>estructurar_mensaje('', 'Escuela', 'se realizaron avances los caules se exponeran a continuacion....')
        Traceback
         ...
        Exception: Nombre invalido.
    """
    #+"-"+ datee
    id= name+"1"
    print(name,category,datee,body,id)
    print("Exito")
    almacenable = {
        "name": name,
        "category": category,
        "datee": datee,
        "body": body,
        "id": id
    }
    nombre_de_archivo = f"{name}-{category}.json"
    datos = store_string(
        "noteplane/notes",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos


#Update nota
def update_n(datee=None, name=None, category=None, body=None):
    """
        Funcion para actualizar una nueva nota
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
    id= name +"-"+ datee
    print("Desde Modulo store")
    print(name,category,datee,body,id)
    print("Exito")
    almacenable = {
        "nombre": name,
        "category": category,
        "date": datee,
        "body": body,
        "id": id
    }
    nombre_de_archivo = f"{name}-{category}.json"
    datos = store_string(
        "noteplane/notes",
        nombre_de_archivo,
        json.dumps(almacenable),
        update=True
    )
    return datos

"""
    Funcion para consultar una nota
    trabaja con el argumento

     - id, Una cadena de texto autogenerada que corresponde a una nota (solo existe una id por nota y esta no debe repetirse).

    Solo acepta una id creada argumento mediante la solicitud curl

    Esta funcion regresara un diccionario con todas las notas que se encuentren almacenadas.
"""
#consultar nota espesificas
def afun(id=None):
    query_result = query_storage(
        "noteplane/notes"
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("todo bien")




#Consultar notas
def query_n(notes=None):
    """
        Funcion para consultar una nota
        trabaja con el argumento

         - notes, una cadena de texto que corresponda al nombre de las notes.

        No acepta ningun tipo de argumento mediante la solicitud curl

        Esta funcion regresara un diccionario con todas las notas que se encuentren almacenadas.
    """
    query_result = query_storage(
        "noteplane/notes",
    )
    return query_result["content"]



## Create category
def create_c(name=None, summary=None):

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

    print("Desde Modulo store")
    print(name, summary)
    print("Exito")
    almacenable = {
        "name": name,
        "summary": summary
    }
    nombre_de_archivo = f"{name}-{summary}.json"
    datos = store_string(
        "noteplane/category",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos


#consulta categorias
def query_c(notes=None):
    """
        Funcion para consultar una categoria
        trabaja con el argumento

         - category, una cadena de texto que corresponda al nombre de las categorias.

        No acepta ningun tipo de argumento mediante la solicitud curl

        Esta funcion regresara un diccionario con todas las las categorias que se encuentren creadas y almacenadas.
    """
    query_result = query_storage(
        "noteplane/category",
    )
    return query_result["content"]
