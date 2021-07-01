# Note-Plane

## En que consiste Note-Plane
  La principal funcion de Note-Plane es el poder crear, almacenas y consultar notas en un formato de texto plano de la manera mas simple posible, y que se pueda acceder desde cualquier navegador para poder tener tus notas disponibles en todo momento.



## Rutas de la API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/note-plane/consult`           | Se podran consultar las notas almacenadas con su nombre            |
| `/note-plane/consult/<key>`           | Se podran consultar las notas almacenadas con una palabra clave            |
| `/note-plane/consult/<creator>`       | Se mostraran las notas de un creador en espesifico           |
| `/note-plane/creator/`       | Se mostraran los creadores de notas           |
| `/note-plane/note-info/<name>`            | Se mostrara toda la informacion relacionada a la nota seleccionada            |
| `/note-plane/date`            | Se mostrara la fecha de creacion de la nota            |
| `/note-plane/create/note`            | Se podran crear notas            |

---
Otro partado en proceso, andamos en obra negra aun
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
##### Operaciones de Notas
- Cear una nota
  - Solicitar Titulo de nota y categorias
  - Solicitar contenido de la nota
  - El identificador se agregara de manera automatica
- Editar una nota
  - Eliminar una nota
  - Cambiar contenido de una nota

#### Operaciones de profes
###### Registrar un Profe
  - solicitamos nombre, edad y titulo
  - numero de empleado sera asignado de manera automatica ya que sera nuestro identificador unico

##### Operaciones de materias
###### Registrar una materia
solcitiamos nombre de la materia, clave, numero de empleado del profesor, y periodo en que sera impartida

##### Operaciones de Calificaciones
###### Registrar a un alumno en el curso
- Solicitamos periodo, materia_clave, profe_no_emp, matricula del alumno.
###### Registrar calificación para un alumno
- Solicitamos periodo, materia_clave, matricula del alumno, y calificación


Esta es la manera en la cual almacenaremos los datos.

Operaciones de consulta de datos
Solicitar datos de un alumno
básicos
con cursos
con cursos activos
todas las calificaciones
calificaciones por periodo
Solicitar datos de un profe
básico
con historial de materias
con materias activas materias
Solicitar datos de una materia
Lista de profes
Activos
Todos
Lista de Alumnos
Activos
Por Materia
Todos
Lista de Materias
Por Periodo
Todos
Con datos del profesor
Con resumen de alumnos
Estructuras de solicitud y respuesta
Registro de alumno
{
    "nombre": "Juanito Johns",
    "fecha_de_nacimiento": "1990-01-01"
}
Respuesta de registro de alumno exitoso
{ "matricula": "XX-XX-XX-00" }
Mensaje de fallo
{
    "code": 500,
    "message": "mensaje de error"
}
Pendiente

Implementación de rutas para los recursos
POST /alumno
recibe una estructura de registor de alumo
201, registrar alumno regresa estructura de matricula para nuevo alumno
D.O.M, regresa estructura de mensaje de fallo
GET /alumno/listar
200 regresa una lista de alumnos
D.O.M, regresa mensaje de fallo en formato json
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
Para hacer peticiones HTTP podemos utilizar diversas herramientas, como puede ser POSTMAN, el modulo requests de python o curl mismo.

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
