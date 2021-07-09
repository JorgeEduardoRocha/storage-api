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

## Historial de git

```

commit a2bc917d97c0c1afd62384ab8acdaf404ae68fab
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Wed Jul 7 15:54:53 2021 -0700
    Update en campos
    introduccion y definicion de proyecto
    formatos de presentaciones generales


commit 89e0f98de4c11f57a6aa5bc83ec589b87eeb400e
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Tue Jul 6 15:30:44 2021 -0700
    ejemplos de uso


commit 447f9b44ef05fcc0b473aee164b0d4344cf5a839
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Tue Jul 6 10:18:24 2021 -0700
    descripcion general


commit 38956fc244442f8ad2ebacc1a1a5a4681295eb11
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Sat Jul 3 12:56:58 2021 -0700
    formato tabla


commit f9c44491c42ff3162d718831623e8661b234a2cc
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Thu Jul 1 18:40:50 2021 -0700
    correccion en info


commit b7b94a123872619b1e88825d5fefc293e5aa77dc
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Thu Jul 1 18:40:02 2021 -0700
    query


commit ea51b1146539c5335851106ceb13d66fbb012303
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Thu Jul 1 15:09:21 2021 -0700
    Cambias mayores en estrutura, sobre todo en acciones


commit 17f8de0d0c3b1f5a857afe0110f40bb3569366c1
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Thu Jul 1 14:57:09 2021 -0700
    crear nota


commit 5bff4a7410626408c52ebb7e5ede3fd73f4eb2ff
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Thu Jul 1 14:51:57 2021 -0700
    categoria


commit 05e4eefe404156653c1a1e0664a1e0ca64382747
Author: rocha <rochanunezjorgeeduardo@gmail.com>
Date:   Thu Jul 1 14:49:17 2021 -0700
    info de creador


commit 0e71982dfe4aaf77286f797a81f99c470feed09c (Rocha/master)
Author: unknown <rochanunezjorgeeduardo@gmail.com>
Date:   Tue Jun 29 15:10:26 2021 -0700
    Trabajo en archvos PY de note-plane v1


commit 1172e7c09f026f310215722d77fc1a89d058a539
Author: unknown <rochanunezjorgeeduardo@gmail.com>
Date:   Fri Jun 25 15:21:47 2021 -0700
    add md


```


# Computo en la nube


### Fork del proyecto y creacion de MD principal.

- Se realizo el un fork con el programa principal, ademas de que se creo el MD principal del proyecto.

| Accion                | Commit Hash|
| --------------------- | ----------- |
| Crear fork y agregar md | 1172e7c09f026f310215722d77fc1a89d058a539 |
| Crear fork y agregar md | c67da9a4aad76ef6d49032dab4aa4a3c482b1784 |


---


### Creacion de archivos de funcionamiento
- Archivos agregados en las siguentes rutas
    - `./docs`
    - `./routes`
    - `./modules`
    - `./models`

#### Definicion de archivos

###### docs
se crearon documentos relacionados a la documentacion de proyecto como `note-plane.md`.

###### routes
Se crearon documentos formato py como `note-plane.py` los cuales contienen el codigo necesario para poder ejecutar las funciones.

###### modules
Se crearon modulos de codigo en formato py como `note-plane.py` en el cual se definieron funciones para realizar acciones espesificas que requiere el poryecto como, almacenamiento, autentificacion y funcionalidad general de consulta y creacion.

###### models
Se creron documentos que corresponden a los modelos que tomara el proyecto como el documento `base.py` el cual corresponde a un modelo de almacenamiento en base de datos, se agrego el documento `note-plane-models.py`.


| Accion                | Commit Hash|
| --------------------- | ----------- |
| Trabajo en archvos PY de note-plane v1 | 0e71982dfe4aaf77286f797a81f99c470feed09c |
| definicion de rutas, crear archivos    | 2e7588d6f1a4d87a03f3687552be7896a500bc08 |

---


### Creacion de rutas espesificas

- Se crearon rutas las cuales tienen que responder 501, con Content-Type: application/json, y un cuerpo de respuesta en formato json con 2 llaves, code y message, el message, Not Implemented.

- Entregable, señalar el commit-hash que contiene la codificacion de las rutas.

| Accion                | Commit Hash|
| --------------------- | ----------- |
| Respuesta de creacion | 1172e7c09f026f310215722d77fc1a89d058a539 |

---


### Funcionamiento de almacenamiento de archivos
Se mostraran ejemplo de funciones simuladas con resulados preestablecidos, con el proposito de crear una base al funcionamieno real
que se desea obtener

- se generaron simulaciones de las acciones del proyecto

- Se utilizar una funcion para acceder a un archivo ya existente para consultarlo


| Accion                | Commit Hash|
| --------------------- | ----------- |
|  Codificacion de funciones |   1172e7c09f026f310215722d77fc1a89d058a539 |
---


### Esquemas de interfaz web del proyecto

- En `note-plane-0000-Dashboard principal` se muestra el dashboard principal de la interfaz web.
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/1b97f54621cf5048f35a5b99e95b3b7a7d7ecab4/docs/assets/note-plane-0000-Dashboard%20principal.png" width="550">  

- EN `note-plane-0001-Crear nota` se muestra la interfaz para crear una nota asi como los elementos solicitados.
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0001-Crear%20nota.png" width="550">  

- En `note-plane-0002-Crear categoria` se muestra la interfaz para crear una categoria asi como los elementos solicitados.
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0002-Crear%20categoria.png" width="550">  

- En `note-plane-0003-Vizualizar nota seleccionada` Se muestra una nota de forma espesifica tanto para consultarla como para comenzar a trabajar en ella.
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0003-Vizualizar%20nota%20seleccionada.png" width="550">  


| Accion                | Commit Hash |
| --------------------- | ----------- |
|  Creacion de MoqUps y definicion | 4fdef40976e90f67f806028e9f551d726b5d4df0 |
