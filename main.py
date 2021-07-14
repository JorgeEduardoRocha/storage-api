"""Simple API

This is a working example of a simple api done with
bottle.py and intended to be used as a Google Cloud Run
service.

"""
<<<<<<< HEAD
<<<<<<< HEAD

import sys
import datetime
=======
>>>>>>> ca8357a (Se crearon rutas espesificas)
=======
=======

import sys
import datetime
>>>>>>> 46ceba701515c021443defe76eb102e29381238e
>>>>>>> 8e3816a9228fe719e38aa2ee6bfd306939833f66
import bottle
import routes.auth
import routes.storage
import models.base

app = bottle.Bottle()

app.mount("/auth", routes.auth.app)
app.mount("/storage", routes.storage.app)


@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)


if __name__ == '__main__':
    error = False
    if (argv_len := len(sys.argv)) > 1:
        if sys.argv[1] == 'routes':
            for route in app.routes:
                print(route.rule, route.method, route, sep="\t")
        if sys.argv[1] == 'db' and 'migrate' in sys.argv:
            print("Database Migration:")
            now_iso = datetime.datetime.utcnow().isoformat()
            models.base.migrate_database(now_iso)
        else:
            error = True
    elif error:
        print("Bad use")
    else:
        app.run(host="0.0.0.0", port=8080)
