### Note-Plane

# Planeacion de proyectos

## Introduccion a Note-Plane

La principal funcion de Note-Plane es el poder crear, almacenas y consultar notas en un formato de texto plano de la
manera mas simple posible, y que se pueda acceder desde cualquier navegador para poder tener tus notas disponibles en
todo momento.

El enfoque de este proyecto es un nicho de personas que quieren una manera simple de crear,
consultar y almacenar notas en formato de texto plano y sobre todo tener la posibilidad de poder acceder a ellas desde
mayor cantidad de dispositivos posibles en todo momento.


---
## ¿Que es Note-plane?

### Motivaciones y proposito de Note-plane

La principal motivacion para desarrolar este proyecro es el de poder tener la capacidad de administrar de mejor manera nuestras
notas de texto plano y poder tenerlas en todo momento y en todo sitio, con el proposito de poder ser una alternativa solida
al momento de pensar en notas online.

### Razon de ser de Note-Plane
A continuacion se contestaran algunas preguntas que pueden surgir al respecto de este proyecto.

- ¿Quien es el publico objetivo de este proyecto?
Desde luego este proyecto tiene in publico definido bastante claro, son las personas que realizan sus notas de esta manera, se
les propone el poder hacerlo de manera distinta y preferentemente mas atrativa.

- ¿Cual es la solucion especifica que plantea este proyecto?
La falta de centralizacion de notas, el no tener algunas notas en un dispotivo en el cual las ocupas. aunque parece simple puede
llega a significar un tiempo considerable el estar reuniendolas a largo plazo, se intenta evitar esto.


- ¿Que recursos se necesitan para iniciar trabajo sobre este proyecto? (Recurso humano, recurso de computo, infrestructura para el despligue)
  - Dispositivo con conexion a internet
  - ordenador capas de correr codigo de python y un entorno http
  - Persona con conocimeinto basico en formatos json, http, python y


- ¿Que se ocupara hacer una ves se implemente el proyecto?
Solo sera necesario empezar a crear y consultar tus notas en todo momento y lugar.

---


## API
#### Application Programing Interface

Entidades con las cuales funcoonara la API

- Nota (clave, titulo, fecha, informacion de creacion, contenido)
- Creador (nombre, nickname, correo, contasena)
- Categoria (clave, nombre)


---
## CRUD (Create, Read, Update, Delete).

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


#### Operaciones de consulta de datos

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
## Estructuras de solicitud y respuesta

### Registro de nota
```          {
              "titulo": "nota de ejemplo",
              "categoria": "",
              "contenido": "",
          }
```

### Respuesta de registro de nota exitoso
```          {
              "code": 201,
              "message": "Nota creada exitosamente"
          }
```

### Mensaje de fallo
```          {
              "code": 500,
              "message": "No se pudo crear la nota"
          }
```

### Registro de Categoria
          ```{
              "nombre": "Eletronica",
              "descripcion": "En esta categoria se hablara de temas telacionadas con eletronica",
          }
          ```

### Respuesta de categoria creada exitosamente
```          {
              "code": 201,
              "message": "Categoria creada exitosamente"
          }
```

### Respuesta de error al crear categoria
```          {
              "code": 500,
              "message": "No se pudo crear la catefgoria"
          }
```


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
- Recibe el identificador correspondiente a uno nota
- 200 regresa la nota que corresponda
- D.O.M, regresa mensaje de nota no encontrada 404

### GET /query/<creador>
- Recibe el nombre del creador
- 200, regresa la nota que correspondan a ese creador
- D.O.M, regresa mensaje de creador no encontrado

### GET /query/category
- 200, regresa la nota que correspondan a esa categoria
- D.O.M, regresa mensaje de categoria no encontrada

### GET /query/<name>
- Recibe el nombre de una nota
- 200, regresa la nota que correspondan a ese nombre
- D.O.M, regresa mensaje de fallo en formato json

### GET /category/<name>
- Recibe el nombre de alguna categoria existente
- 200, regresa las notas que correspondan a esa categoria
- D.O.M, regresa mensaje de fallo general

### POST /create/category
- 201, registrar una nueva categoria
- D.O.M, regresa mensaje de fallo

### GET /info/<key>
- Recibe el identificador de una nota
- 200, Datos detallados de la nota espesifica que corresponda a la key escrita
- D.O.M, regresa mensaje de contenido enextitente (404)
---


## Ejemplos de consultas
---
### DATA=$(cat /path/to/file)
```
          curl -qv \
              ${URL_HOST}${ROUTE} \
              -X ${METHOD} \
              -H "${HEADER_1}" \
              -H "${HEADER_2}" \
              -d "$DATA"
```
>Estrutura basica de interaccion

- Solicitar Titulo de nota y categorias(opcional)
- Solicitar contenido de la nota(opcional)
- El identificador se agregara de manera automatica

### ejemplo de creacion de nota
En este ejemplo se agregara una nota,
primero se requiere conectar al servidor donde se encuentre corriendo el programa y posteriormente, definir la ruta que se
utilizara, depues de esto el programa requiere resibir un usuario para poder crear la nota,
 para esto el programa valida al usuario
(determina si es posible para el usuario crear la nota o no), despues de eso se solicita la informacion de la nota
siendo la unica implesindible el nombre de la nota pudiendo ir los otros dos cambos vacios por el momento, y al momento de
crear la nota se agregara un identificador reconocido como  `KEY`, con esto ya se tendra la nota creada


```
- URL_HOST=http://localhost:8080
- ROUTE=/note/create
- METHOD=POST
- HEADER_1='Content-Type: application/json'
- HEADER_2="Authorization: Bearer ${TOKEN}"
- DATA='{"name":"nota de ejemplo", "category":"Robots",
        "content":""
        }'
```


## Usuarios y autentificacion

- (Administrador) Leer todo, editar solo las notas propias: (app: notes:read:all, app: notes:write:self)
- (Usuario) Leer todo, y editar todo (Usuario): (app: notes:read:all, app: notes:write:all)

>Solo se tomaran estos usuarios para trabajar


## Archivos Relacionados

- `routes/note-plane.py`
- `routes/auth.py`
- `routes/storage`


## Almacenamiento

Todas las notas seran en formato JSON y se almacenaran de manera local o en almacenamiento en nube (Almacenamiento deseable).
>Se recomienda utilizar almacenamiento en nube por el objetivo del Note-plane al ser lo que mas apropiado

## Prefijos de almacenamiento:

 - `note-plane/`

# Computo en la nube
