# Taller de programación Web con Tornado para alumnos de primer año

Este es un taller de introducción a la programación Web
diseñado para alumnos de primer año de Ingeniería. Como
*framework* Web y servidor, se utiliza la librería de Python
Tornado.

El objetivo del taller es la elaboración de una aplicación
Web para gestionar una lista de compras. Para lograrlo se
utiliza sólo HTML, Python y los recursos que entrega
Tornado.

El taller está organizado en partes, las cuales agregan
funcionalidad incrementalmente a la aplicación.

# Partes

## Parte 1

La parte 1 muestra un documento HTML estático básico en el
cual se detalla una lista de compras.

## Parte 2

La parte 2 mantiene el mismo archivo HTML de la parte 1.
Esta vez se añade un servidor mínimo de Tornado que atiende
consultas en el puerto 50000 y responde con el HTML
desarrollado en la parte 1.

Para iniciar la aplicación es necesario ejecutar el
siguiente comando:

    python3 server.py

Para ver la página se puede acceder a
<http://localhost:50000/lista>.

## Parte 3

La parte 3 pretende introducir los *templates* disponibles
en Tornado. En este caso el servidor define una lista dentro
del *template*, la cual es recorrida para generar el HTML
necesario para mostrar al usuario cada elemento de la lista.

## Parte 4

En la parte 4 se agrega un formulario que permite introducir
dinámicamente elementos en la lista desde el cliente. Esto
se logra utilizando el método POST de HTTP.

## Parte 5

En esta parte se agrega un botón que permite borrar los
elementos seleccionados. Además se introducen los controles
ocultos (`<input type="hidden">`), que permiten identificar
la operación que se desea realizar sobre los datos (agregar
o borrar).

# To do

- [ ]   Agregar enlaces a la documentación de Tornado y
        HTML.
- [ ]   Hacer una parte que agregue soporte para móviles,
        cambiando el tamaño del *viewport*.
- [ ]   Hacer una parte que agregue una protección de
        edición múltiple basada en versiones.
- [ ]   Hacer una parte que impida elementos duplicados.
- [ ]   Agregar CSS.
- [ ]   Agregar soporte para el método PATCH, utilizando
        AJAX.
- [ ]   Agregar documentación de funciones.
- [ ]   Mejorar el manejo de errores.
- [ ]   Agregar soporte para virtualenv.
- [ ]   Agregar soporte para heroku.
