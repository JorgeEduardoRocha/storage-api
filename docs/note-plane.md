### Note-Plane

# Estructura general de proyecto
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
- Creador (nombre, credenciales)
- Categoria (clave, nombre, descripcion)



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
  - Solicitar contenido de la nota(opcional)
  - El identificador se agregara de manera automatica
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
  - nombre

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
```         
{
 "titulo": "nota de ejemplo", "categoria": "", "contenido": ""
}
```

### Respuesta de registro de nota exitoso
```         
{
"code": 201, "message": "Nota creada exitosamente"
}
```

### Mensaje de fallo
```          
{
"code": 500, "message": "No se pudo crear la nota"
}
```

### Registro de Categoria
```
{
"nombre": "Eletronica", "descripcion": "En esta categoria se hablara de temas telacionadas con eletronica"
}
```

### Respuesta de categoria creada exitosamente
```          
{
"code": 201, "message": "Categoria creada exitosamente"
}
```

### Respuesta de error al crear categoria
```
{
"code": 500, "message": "No se pudo crear la catefgoria"
}
```

---



## Rutas de la API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/noteplane/create_note`           | Crear una nota completamente nueva |
| `/noteplane/update`                | Actualizar una nota ya existente |
| `/noteplane/<id>`                  | Regresa una nota en espesifico |
| `/noteplane/query/notes`           | Regresa todas las notas disponibles |
| `/noteplane/create_category`       | Crear una nota completamente nueva |
| `/noteplane/query/category`        | Regresa todas las nota creadas |


---
agregar verbos HTTP ^
---

## Implementación de rutas para los recursos

### POST /create_note
- Recibe datos de creacion de notas
- 201,Crear nota y regresar identificador de la nota
- D.O.M, regresa estructura de mensaje de fallo

### POST /update
- Recibe datos de creacion de notas
- 201,Crear nota y regresar identificador de la nota
- D.O.M, regresa estructura de mensaje de fallo

### GET /query/notes
- 200, regresa la nota que correspondan a esa categoria
- D.O.M, regresa mensaje de nota no encontrada 404

### GET / < id >
- Recibe el nombre de la nota
- 200, regresa la nota que correspondan a ese creador
- D.O.M, regresa mensaje de creador no encontrado

### GET /query/category
- 200, regresa la nota que correspondan a esa categoria
- D.O.M, regresa mensaje de categoria no encontrada


### POST /noteplane/create_category
- Recibe datos de creacion de categorias
- 201, registrar una nueva categoria
- D.O.M, regresa mensaje de fallo

---



## Ejemplos de consultas

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
URL_HOST=http://localhost:8080 \
ROUTE=/note/create \
METHOD=POST \
HEADER_1='Content-Type: application/json' \
HEADER_2="Authorization: Bearer ${TOKEN}" \
DATA='{"name":"nota de ejemplo", "category":"Robots", "content":""}' \
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



# Documento tecnico de funcionamiento general


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
>Seccion en desarrollo

- Se crearon rutas las cuales tienen que responder 501, con Content-Type: application/json, y un cuerpo de respuesta en formato json con 2 llaves, code y message, el message, Not Implemented.

- Rutas creadas, falta implementacion de codigo completo  

| Accion                | Commit Hash|
| --------------------- | ----------- |
| Respuesta de creacion | ca8357af36ef4b3ed72de88b6e8111a09153271f  |

---


### Funcionamiento de almacenamiento de archivos
>Seccion en desarrollo

Se mostrara uan simulacion del funcionamiento esperado del proyecto con el proposito de poder visualizar como es que se comportara el poryecto una vez conlcuido, y para observar detalladamente el funcionamiento del almacenamiento de archivos

- se generaron simulaciones de las acciones del proyecto

- Se utilizar una funcion para acceder a un archivo ya existente para consultarlo


| Accion                | Commit Hash|
| --------------------- | ----------- |
|  Codificacion de funciones | f5080c2015adc53ed0e53d9454592cc1489c2089 |
---


### Esquemas de interfaz web del proyecto

- En `note-plane-0000-Dashboard principal` se muestra el dashboard principal de la interfaz web.
  - boton buscar: se mostrara una barra de busqueds y despues solo las notas que coicidan
  - boton de eliminar: se Mostra uns ventana emergente para confirmar sl eliminar el elemento
  - boton editar: se direccionara a la ventana de lectura y edición general de notas `note-plane-0003-Vizualizar nota seleccionada`

<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/1b97f54621cf5048f35a5b99e95b3b7a7d7ecab4/docs/assets/note-plane-0000-Dashboard%20principal.png" width="550">  



- EN `note-plane-0001-Crear nota` se muestra la interfaz para crear una nota asi como los elementos solicitados.
  - se solicitan datos generales para generar una nota (solo el nombre es obligatorio al momento de crear una nota)

<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0001-Crear%20nota.png" width="550">  



- En `note-plane-0002-Crear categoria` se muestra la interfaz para crear una categoria asi como los elementos solicitados.
  - se solicitan datos generales para crear una nota (solo el nombre es obligatorio al momento de crear una nota)

<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0002-Crear%20categoria.png" width="550">  



---  
- En `note-plane-0003-Vizualizar nota seleccionada` Se muestra una nota de forma espesifica tanto para consultarla como para comenzar a trabajar en ella.
  - en esta sección se pueden leer las notas generadas, además de poder dirar todos los campos de la nota.

<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0003-Vizualizar%20nota%20seleccionada.png" width="550" >  



| Accion                | Commit Hash |
| --------------------- | ----------- |
|  Creacion de MoqUps y definicion | 4fdef40976e90f67f806028e9f551d726b5d4df0 |


## Casos de uso

### Crear una nueva nota
- Metodo `Post`
- Objetivo: Crear una nueva nota
- Se requieren ingresar los valores de
  - `name`
  - `date`
  - `category`
  - `Content`
- Si no se ingresa nombre de la nota no se podra crear
- Si la nota tiene el mismo nombre que una nota ya axistente no se podra crear

En esta funcion se crea una nota nueva, ingresando todos los datos correctos.
```
curl localhost:8080/noteplane/create_note -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo final","category":"ejemplo","datee": "2012-12-12", "content":""}'
```


### Actualizar una nota
- Metodo `Post` (sobre json ya existente)
- Objetivo: Actualizar una nota ya existente
- Se requiere ingresar el nombre exacto de la nota que se desea Actualizar
- Si no se ingresa exactamente el nombre de la nota que se desea actualizar no funcionara y marcara errors

En esta funcion se remplaza un json de una nota que se encuentre ya creada, para esto se require el nombre de la nota, que corresponde al nombre del archivo, para poder remplazarla.
```
curl localhost:8080/noteplane/note/update -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo12","category":"ejemplo","datee": "2010-12-12", "content":""}'
```


### consultar Notas
- Metodo `GET`
- Objetivo: Consultar todas las notas que se encuentren disponibles.
- Solo se requiere hacer una consulta a la ruta, no se requiere espesificar ningun parametro

En esta funcion se regresa una lista con los json que conforman todas las notas disponibles.
```
curl localhost:8080/noteplane/query/notes
```


### consultar Notas espesificas
- Metodo `GET`
- Objetivo: Consultar una nota espesifica con su `name`
- Se requiere del `name` de la nota, este dato debe ser exato, en caso de ingresar un `name` no valido, regresara un error y no regresara informacion

En esta funcion se regresa una nota espesifica con su `name` el cual es un valor auto generado, que se genera atravez de la informacion que compone la nota.
```
curl localhost:8080/noteplane/ejemplos1 -X GET
```

### Crear una nueva categoria
- Metodo `POST`
- Objetivo: Crear una categoria nueva
- Se requieren ingresar los siguentes parametros para crear la categoria
  - `name`
  - `description`
- Se requiere ingresar el nombre de la categoria, de otro modo la funcion regresara un error
- Si se ingresa un nombre de categoria que ya existe regresara un error
- Es posible no definir una descipcion para la categoria

En esta funcion se genera un archivo json el cual corresponde a una categoria, con informacion basica para poder identificarla.

```
curl localhost:8080/noteplane/create_category -X POST -H "Content-Type: application/json" -d '{"name": "motores","summary": "todo respecto a carros y motores"}'
```

### consultar Notas
- Metodo `GET`
- Objetivo: Consultar todas las categorias creadas
- Solo se require hacer la consulta en la ruta para obtener una lista de los json que corresponden a cada categoria

En esta funcion se regresaran todas las categorias disponibles.
```
curl localhost:8080/noteplane/query/category
```

# Planeacion para frontend

El proposito de la interfaz grafica es cumplir con los objetivos planteados desde el comienzo del proyecto, con lo que se busca una interfaz de usuario amigable, eficiente y que 
corresponda con las funciones que el proyecto tiene.

las funciones nesesarios son 
- Crear notas
- Crear categorias
- Consultar notas
- Consultar categorias

Con lo dicho anteriormente se planea implementar una interfaz amigable y sobre todo que sea pratica para el usuario, por la naturaleza del proyecto y al ser algo tam simple como
el crear notas es evidente que cualquier contratiempo al momento de crearlas podria ser una molesta mayor que simplemente utilizar el primer metodo que se tenga a disposicion.

#### Ejemplos de interfaz de usuario

###### para comenzar se planea tener un dashboard de facil acceso como el que se muestra a contiunuacion.
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/1b97f54621cf5048f35a5b99e95b3b7a7d7ecab4/docs/assets/note-plane-0000-Dashboard%20principal.png" width="550">  

Como se puede observar en este dashboard se dan la mayoria de las funciones principales, de esta manera el usuario tiene todo a mano lo mas rapido posible.


###### Creacion de nota
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0001-Crear%20nota.png" width="550"> 

Al igual que en el ejemplo anterior el enfoque esta en no perder tiempo, la interfaz para crear una nota es simple pero duficiente para que no sea un inconveniente el crearla.



###### Editar una nota
<img src="https://github.com/JorgeEduardoRocha/storage-api/blob/24a356148b0e4a677cb8e9a92eb821321529393e/docs/assets/note-plane-0003-Vizualizar%20nota%20seleccionada.png" width="550" >  

En cuento a editar una nota se otorna un espacio optimo para poder trabajar con la nota y da la oportunidad de cambiar todos los datos de la nota en el mismo sitio.


### Objetivo
El objetivo del frontend de Note-plane es el ser una herramienta pratica para el usuario, de manera que se intentara evitar cualquier problema que los usaurio puedan tener,
ademas en el futuro se planea hacer mejoras en este aspecto, como tener elemento ajustables, todo con el proposto de facilitar una tarea que muchas personas hacen sin ningun 
tipo de herramienta espesifica como esta.
