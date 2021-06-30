# Note-Plane

## En que consiste Note-Plane
  La principal funcion de Note-Plane es el poder crear, almacenas y consultar notas en un formato de texto plano de la manera mas simple posible, y que se pueda acceder desde cualquier navegador para poder tener tus notas disponibles en todo momento.



## API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/note-plane/consult`           | Se podran consultar las notas almacenadas con su nombre            |
| `/note-plane/consult/<key>`           | Se podran consultar las notas almacenadas con una palabra clave            |
| `/note-plane/consult/<creator>`       | Se mostraran las notas de un creador en espesifico           |
| `/note-plane/creator/`       | Se mostraran los creadores de notas           |
| `/note-plane/note-info/<name>`            | Se mostrara toda la informacion relacionada a la nota seleccionada            |
| `/note-plane/date`            | Se mostrara la fecha de creacion de la nota            |
| `/note-plane/create/note`            | Se podran crear notas            |

Como

# Archivos Relacionados

 - `routes/note-plane.py`

Prefijos de almacenamiento:

 - `note-plane/`

Tablas de Base de Datos

> Pendiente o Nulo
