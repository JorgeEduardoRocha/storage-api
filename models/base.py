from os import environ, chdir
import peewee as pe
import peewee_migrate as pm


def get_database():
    _type = environ.get("DATABASE_TYPE", "sqlite")
    name = environ.get("DATABASE_NAME", "database.db")
    options = dict(
        host=environ.get("DATABASE_HOST", "localhost"),
        user=environ.get("DATABASE_USER", None),
        password=environ.get("DATABASE_PASSWORD", None),
        port=int(environ.get("DATABASE_PORT", 0)),
    )
    if _type == 'sqlite' and name:
        return pe.SqliteDatabase(name)
    elif _type == 'postgresql':
        options["PORT"] = options["PORT"] or 5432
        return pe.PostgresqlDatabase(name, **options)
    elif _type == 'mysql':
        options["PORT"] = options["PORT"] or 3306
        return pe.MySQLDatabase(name, **options)
    raise Exception("No database defined")


class EnvModel(pe.Model):
    class Meta:
        database = get_database()


def migrate_database(name):
<<<<<<< HEAD
<<<<<<< HEAD
    router = pm.Router(get_database())
    router.create(name)
    router.run()
=======
=======
>>>>>>> 2e7588d (definicion de rutas CELN)
    if name:
        # chdir("./models")
        router = pm.Router(get_database())
        router.create(name, auto=True)
        router.run(name)
    else:
        print("please provide with a name")
<<<<<<< HEAD
>>>>>>> 2e7588d (definicion de rutas CELN)
=======
>>>>>>> 2e7588d (definicion de rutas CELN)
=======
    if name:
        # chdir("./models")
        router = pm.Router(get_database())
        router.create(name, auto=True)
        router.run(name)
    else:
        print("please provide with a name")
=======
    router = pm.Router(get_database())
    router.create(name)
    router.run()
>>>>>>> 46ceba701515c021443defe76eb102e29381238e
>>>>>>> 8e3816a9228fe719e38aa2ee6bfd306939833f66
