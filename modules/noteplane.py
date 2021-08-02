"""
Trabajo en progreso de modelos nesesarios
"""
import json
from datetime import datetime
from modules.storage import (
    store_string, store_bytes,
    query_storage, get_storage_file
)






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
#create note
def create_n(fecha=None, name=None, category=None):
    id= name +"-"+ fecha
    print("Desde Modulo store")
    print(name,category,fecha,id)
    print("Exito")
    almacenable = {
        "nombre": name,
        "category": category,
        "fecha_de_ingreso": fecha,
        "id": id
    }
    nombre_de_archivo = f"{name}-{category}-{fecha}-{id}.json"
    datos = store_string(
        "noteplane/notes",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

#Update note
def update_n(fecha=None, name=None, category=None):
    id= name +" "+ fecha
    print("Desde Modulo store")
    print(name,category,fecha,id)
    print("Exito")
    almacenable = {
        "nombre": name,
        "category": category,
        "fecha_de_ingreso": fecha,
        "id": id
    }
    nombre_de_archivo = f"{name}-{category}-{fecha}-{id}.json"
    datos = store_string(
        "noteplane/notes",
        nombre_de_archivo,
        json.dumps(almacenable),
        update=True
    )
    return datos

#consultar nota espesificas
def query_n_s(id=None):
    query_result = query_storage(
        "noteplane/notes",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("todo bien")

#Consultar notas
def query_n(movies=None):
    query_result = query_storage(
        "noteplane/notes",
    )
    if movies is None:
        return query_result["content"]


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
## Create category
def create_c(name=None, summary=None):
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

#update categorias
## update category
def update_c(name=None, summary=None):
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
        json.dumps(almacenable),
        update=True
    )
    return datos


#consulta categorias
def query_c(movies=None):
    query_result = query_storage(
        "noteplane/category",
    )
    if movies is None:
        return query_result["content"]
