# Note-Plane

## En que consiste Note-Plane
  La principal funcion de Note-Plane es el poder crear, almacenas y consultar notas en un formato de texto plano de la manera mas simple posible, y que se pueda acceder desde cualquier navegador para poder tener tus notas disponibles en todo momento.





---
apartado reservado para presentacion
---


# API
#### Application Programing Interface

Entidades con las cuales funcoonara la API

- Nota (clave, titulo, fecha, informacion de creacion, contenido)
- Creador (nombre, nickname, correo, contasena)
- Categoria (clave, nombre)

## CRUD (Create, Read, Update, Delete).

El funcinamiento de la API sera mediante rutas HTTP, con un verbo/método en especifico.

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


## Estructuras de solicitud y respuesta

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



## Rutas de la API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/note/query`           | Se podran consultar las notas almacenadas con su nombre |
| `/note/query/<key>`     | Se podran consultar las notas almacenadas con una palabra clave  |
| `/note/query/<creator>` | Se mostraran las notas de un creador en espesifico |
| `/note/creator/`        | Se mostraran los creadores de notas |
| `/note/info/<name>`     | Se mostrara toda la informacion relacionada a la nota seleccionada   |
| `/note/date`            | Se mostrara la fecha de creacion de la nota |
| `/note/create/note`     | Se podran crear notas |

---
agregar verbos HTTP
---

## Implementación de rutas para los recursos

#### POST /note
- Recibe datos de creacion de notas
- 201,Crear nota y regresar identificador de la nota
- D.O.M, regresa estructura de mensaje de fallo

#### GET /note/id
200 regresa la nota que corresponda
D.O.M, regresa mensaje de nota no encontrada 404


####GET /note/<creador>
200, regresa la nota que correspondan a ese creador
D.O.M, regresa mensaje de creador no encontrado 
---
>
GET /alumno/<matricula>
200, datos de alumno con matricula
D.O.M, regresa mensaje de fallo en formato json
POST /docente
201, regitrar un profe, y regresar numero de emplado
D.O.M, regresa mensaje de fallo
GET /docente/list
200, lista de profes en formato json
D.O.M, regresa mensaje de fallo
GET /docente/<no_emp>
200, datos de un profe por numero de empleado
D.O.M, regresa mensaje de fallo
POST /materia
201, registrar una materia y regresa confirmacion de registro
D.O.M, regresa mensaje de fallo
POST /materia/<periodo>/<clave>/<matricula>/registrar
201, Registrar alumno a una materia
D.O.M, regresa mensaje de fallo
POST /materia/<periodo>/<clave>/<matricula>/calificar
201, asignar una calificacion a un alumno
D.O.M, regresa mensaje de fallo
Ejemplo para el uso de curl
Para hacer peticiones HTTP podemos utilizar diversas herramientas, como puede ser POSTMAN, el modulo requests de python o curl mismo.<
---

curl es un programar que se utiliza en una terminal tipo posix, por lo tanto adoptaremos notacion de archivo de script para un shell posix.

URL_HOST=http://localhost:8080
ROUTE=/test
METHOD=POST
HEADER_1='Content-Type: application/json'
HEADER_2="Authorization: Bearer ${TOKEN}"
DATA='{"data":"foo"}'
# DATA=$(cat /path/to/file)

curl -qv \
    ${URL_HOST}${ROUTE} \
    -X ${METHOD} \
    -H "${HEADER_1}" \
    -H "${HEADER_2}" \
    -d "$DATA"

# Archivos Relacionados

 - `routes/note-plane.py`

Prefijos de almacenamiento:

 - `note-plane/`

Tablas de Base de Datos

> Pendiente o Nulo
