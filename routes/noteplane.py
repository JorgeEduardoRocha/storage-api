import bottle
from bottle import route, run, post, request
from modules.bottles import BottleJson
from modules.noteplane import creador_nota, creador_categoria
app = BottleJson()
@app.get("/")

#ejemplos
@app.get("/foo")
def foo(*args, **kwargs):
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501,"error")

@app.post("/bar")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    raise HTTPError(501)

@app.get("/noteplane/test")
def index():
    payload = bottle.request.query
    print(bottle.request.query_string)
    print(payload.dict)
    raise bottle.HTTPError(501, 'algo salio mal')
    #return dict(code=501, message="not implemented")



##consultar notas (todas las notas)
#el proposito de esta funcion es poder consultar todas las notas a las que la persona que realize
#la consulta pueda acceder
@app.get("/query/notes")
def query(*args, **kwargs):
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    try:
        nombre = str(payload['nombre'])
        categoria = str(payload['categoria'])
        contenido = str(payload['contenido'])
        print("Datos correctos")
        raise bottle.HTTPError(201)
    except:
        raise bottle.HTTPError(501, "Informacion no valida")
    raise bottle.HTTPError(500, "Error general")






#search note by key
#regresar unformacion detallada de una nota en espesifico buscada por su 'ID'
@app.get("/query/<key>")
def query_key(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        print("ID valida")
        respuesta = query_information(**payload)
        raise bottle.HTTPError(201)
    except:
        raise bottle.HTTPError(501, "ID invalida")
    raise bottle.HTTPError(500, "Error general")




#Crear una nueva nota
@app.post("/create")
def generator(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
        #movie_id: int(payload['movie_id'])
        nombre = str(payload['nombre'])
        categoria = str(payload['categoria'])
        contenido = str(payload['contenido'])
        fecha = str(payload['fecha'])
        id = str(payload['id'])
        respuesta = creador_nota(**payload)
        raise bottle.HTTPError(201, "Creada correctamente")
    except:
        raise bottle.HTTPError(400, "Error de datos, no se pudo crear la nota")
    raise bottle.HTTPError(500,"Error general")



#information
#@app.get("/info/<name>")
#def info(*args, **kwargs):
    #aqui codigo
#    return dict(code=501, message="not implemented")

#create category
@app.get("/create/category")
def category_creator(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")

#category spesific
@app.get("/category/<name>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented")
