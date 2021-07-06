# Note-Plane

## Introduccion a Note-Plane

La principal funcion de Note-Plane es el poder crear, almacenas y consultar notas en un formato de texto plano de la
manera mas simple posible, y que se pueda acceder desde cualquier navegador para poder tener tus notas disponibles en
todo momento.

El enfoque de este proyecto es un nicho de personas que quieren una manera simple de crear,
consultar y almacenar notas en formato de texto plano y sobre todo tener la posibilidad de poder acceder a ellas desde
mayor cantidad de dispositivos posibles en todo momento.


---
# ¿Que es Note-plane?

### Motivaciones y proposito de Note-plane


### Razon de ser de Note-Plane

---


# API
#### Application Programing Interface

Entidades con las cuales funcoonara la API

- Nota (clave, titulo, fecha, informacion de creacion, contenido)
- Creador (nombre, nickname, correo, contasena)
- Categoria (clave, nombre)


---
# CRUD (Create, Read, Update, Delete).

### Operaciones de Almacenamiento de datos


#### Operaciones de Notas
###### Cear una nota
  - Solicitar Titulo de nota y categorias(opcional)
  - Solicitar contenido de la nota(opcional)
  - El identificador se agregara de manera automatica
###### Editar una nota
  - Cambiar contenido de una nota
###### elimina una nota
  - Eliminar una nota


#### Operaciones de catefgorias
###### Registrar a una categoria
- Solicitamos nombre, descripcion.
###### Eliminar una categoria
- Eliminar una categoria
###### Editar una categoria
- Cambiar informacion de una categoria


Esta es la manera en la cual almacenaremos los datos.


## Operaciones de consulta de datos

- Consultar notas
  - básicos
  - con fecha
  - con creadore
  - con Titulo
  - identificador

- Consultar creadores  
  - basico
  - identificador
  - nombre
  - username

- Consultar categoria
  - basico
  - identificador
  - nombre
  - conjunto de categorias      

- consultar por filtros
  - basico
  - datos conocidos de la nota
  - texto en el contenido
  - varias categorias
  - filtros en conjuntos espesificos (catefgorias, fecha, nombre, creador)
---

---
# Estructuras de solicitud y respuesta

### Registro de nota
{
    "titulo": "nota de ejemplo",
    "categoria": "",
    "contenido": "",
    "fecha de creacion": "xxxx-xx-xx"
}

### Respuesta de registro de nota exitoso
{ "id": "XXXX" }

### Mensaje de fallo
{
    "code": 500,
    "message": "No se pudo crear la nota"
}

## mas ejemplos despues
---

---
## Rutas de la API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/note/query`           | Se podran consultar las notas almacenadas con su nombre |
| `/note/query/<key>`     | Se podran consultar las notas almacenadas con una palabra clave  |
| `/note/query/<creator>` | Se mostraran las notas de un creador en espesifico |
| `/note/creator/`        | Se mostraran los creadores de notas |
| `/note/info/<name>`     | Se mostrara toda la informacion relacionada a la nota seleccionada   |
| `/note/date`            | Se mostrara la fecha de creacion de la nota |
| `/note/create/category` | Se podra crear una nueva categoria |
| `/note/category/<name>` | Se se mostraran las notas que correspondan a esa categoria |
| `/note/create/note`     | Se podran crear notas |
---

---
## Implementación de rutas para los recursos

### POST /create/note
- Recibe datos de creacion de notas
- 201,Crear nota y regresar identificador de la nota
- D.O.M, regresa estructura de mensaje de fallo

### GET /query/<key>
- 200 regresa la nota que corresponda
- D.O.M, regresa mensaje de nota no encontrada 404

### GET /query/<creador>
- 200, regresa la nota que correspondan a ese creador
- D.O.M, regresa mensaje de creador no encontrado

### GET /query/category
- 200, regresa la nota que correspondan a esa categoria
- D.O.M, regresa mensaje de categoria no encontrada

### GET /query/<name>
- 200, regresa la nota que correspondan a ese nombre
- D.O.M, regresa mensaje de fallo en formato json

### GET /category/<name>
- 200, regresa las notas que correspondan a esa categoria
- D.O.M, regresa mensaje de fallo general

### POST /create/category
- 201, registrar una nueva categoria
- D.O.M, regresa mensaje de fallo

### GET /info/<key>
- 200, Datos detallados de la nota espesifica que corresponda a la key escrita
- D.O.M, regresa mensaje de contenido enextitente (404)
---



curl es un programar que se utiliza en una terminal tipo posix, por lo tanto adoptaremos notacion de archivo de script para un shell posix.


# Ejemplos de consultas
---
## DATA=$(cat /path/to/file)

curl -qv \
    ${URL_HOST}${ROUTE} \
    -X ${METHOD} \
    -H "${HEADER_1}" \
    -H "${HEADER_2}" \
    -d "$DATA"
>Estrutura basica de interaccion<

- Solicitar Titulo de nota y categorias(opcional)
- Solicitar contenido de la nota(opcional)
- El identificador se agregara de manera automatica

## ejemplo de creacion de nota
En este ejemplo se agregara una nota,
primero se requiere conectar al servidor donde se encuentre corriendo el programa y posteriormente, definir la ruta que se
utilizara, depues de esto el programa requiere resibir un usuario para poder crear la nota,
 para esto el programa valida al usuario
(determina si es posible para el usuario crear la nota o no), despues de eso se solicita la informacion de la nota
siendo la unica implesindible el nombre de la nota pudiendo ir los otros dos cambos vacios por el momento, y al momento de
crear la nota se agregara un identificador reconocido como  `KEY`, con esto ya se tendra la nota creada

| URL_HOST=http://localhost:8080
ROUTE=/note/create
METHOD=POST
HEADER_1='Content-Type: application/json'
HEADER_2="Authorization: Bearer ${TOKEN}"
DATA='{"name":"nota de ejemplo", "category":"Robots",
        "content":""
        }' | 

---

# Usuarios y autentificacion
>
- Leer todo, editar solo las notas propias: (app:notes:read:all, app:notes:write:self),
- Leer todo, y editar todo UserA: (app:notes:read:all, app:notes:write:all),

>Solo se tomaran estas validades para trabajar <


# Archivos Relacionados

- `routes/note-plane.py`
- `routes/auth.py`
- `routes/storage`

---
# Almacenamiento

Todas las notas seran en formato JSON y se almacenaran de manera local o en almacenamiento en nube (Almacenamiento deseable).
>Se recomienda utilizar almacenamiento en nube por el objetivo del Note-plane al ser lo que mas apropiado<

## Prefijos de almacenamiento:

 - `note-plane/`
 ---
