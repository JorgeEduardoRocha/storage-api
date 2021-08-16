import bottle
import datetime as dt
from bottle import route, run, post, request
from modules.bottles import BottleJson
from modules.noteplane import  afun, create_n, query_n, create_c, query_c, update_n
app = BottleJson()



## Herramientas de debug
#@app.get("/")


#Crear una nueva nota
# Post crear una nota
# curl localhost:8080/noteplane/create_note -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo12","category":"ejemplo","datee": "2010-12-12", "content":""}'
@app.post("/create_note")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        name = str(payload['name'])
        category = str(payload['category'])
        datee = dt.date.fromisoformat(payload['datee'])
        body = str(payload['body'])
        if len(name) == 0:
            raise Exception()
        print("dato validos")
        respuesta = create_n(**payload)
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)



#Actualizar una nota
# Post sobre un json ya existente
# curl localhost:8080/noteplane/note/update -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo12","category":"ejemplo","datee": "2010-12-12", "body":""}'
@app.post("/update")
def create_category(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        name = str(payload['name'])
        category = str(payload['category'])
        datee = dt.date.fromisoformat(payload['datee'])
        body = str(payload['body'])
        if len(name) == 0:
            raise Exception()
        print("datos validos")
        respuesta = update_n(**payload)
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)




#consultar Notas espesificas
## Get nota espesifica
# curl http://localhost:8080/noteplane/ejemplo1 -X GET
@app.get("/<id>")
def query_ns(*args, id=None, **kwargs):
    try:
        respuesta = afun(id=id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)



#consultar Notas
## Get lista de notas
# curl http://localhost:8080/noteplane/query/notes
@app.get("/query/notes")
def get_notes(*args, **kwargs):
    try:
       respuesta = spesific()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)




#Crear una nueva categoria
# Post crear una categoria
# curl localhost:8080/noteplane/create/category -X POST -H "Content-Type: application/json" -d '{"name": "Juegos","description": "juegos generales, noticias y eventos relacionados"}'
@app.post("/create_category")
def create_category(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        name = str(payload['name'])
        summary = str(payload['summary'])
        if len(name) == 0:
            raise Exception()
        print("dato validos")
        respuesta = create_c(**payload)
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)




#consultar Notas
## Get lista de notas
# curl http://localhost:8080/noteplane/query/category
@app.get("/query/category")
def get_notes(*args, **kwargs):
    try:
       respuesta = query_c()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)
