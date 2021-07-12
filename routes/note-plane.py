from json import dumps as json_dumps
import bottle

STORAGE_METHOD = environ["STORAGE_METHOD"]
if STORAGE_METHOD == 'LOCAL':
    print("Using local storage")
    from modules.storage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
elif STORAGE_METHOD == 'GCLOUD':
    print("Using gcloud storage")
    from modules.gstorage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
else:
    raise Exception("Storage method not set")

app = bottle.Bottle()


<<<<<<< HEAD
<<<<<<< HEAD
@app.get("/query")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)

@app.get("/query/<key>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)

@app.get("/creator")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)

@app.get("/info/<name>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)

@app.get("/create/category")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)

@app.get("/category/<name>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)

@app.get("/create/note")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501, message="not implemented)
=======
@app.get("/store")
=======
@app.get("/query")
>>>>>>> ca8357a (Se crearon rutas espesificas)
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})


@app.get("/query/<key>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})



@app.get("/creator")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})



@app.get("/info/<name>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})


<<<<<<< HEAD
@app.get("/void")
def void_report(*args, **kwargs):
    return dict(code=200)
>>>>>>> 0e71982 (Trabajo en archvos PY de note-plane v1)
=======

@app.get("/create/category")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})


@app.get("/category/<name>")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})


@app.get("/create/note")
def store_record(*args, **kwargs):
    #aqui codigo
    return dict(code=501,{"code" :"501", "messaje" : "Not implement"})
>>>>>>> ca8357a (Se crearon rutas espesificas)
