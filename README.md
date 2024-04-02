## Las ideas de los retos son sacados desde [aqui](https://github.com/mouredev/roadmap-retos-programacion/tree/main)

# 06 - Recursividad
**EJERCICIO:** <br>
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.

**DIFICULTAD EXTRA (opcional):** <br>
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).

# 07 - Pilas y Colas
**EJERCICIO:** <br>
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).

**DIFICULTAD EXTRA (opcional):** <br>
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.

# 08 - Clases
**EJERCICIO:** <br>
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.

**DIFICULTAD EXTRA (opcional):** <br>
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.

# 09 - Herencia
**EJERCICIO:** <br>
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.

**DIFICULTAD EXTRA (opcional):** <br>
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.

# 10 - Excepciones
**EJERCICIO:** <br>
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.

**DIFICULTAD EXTRA (opcional):** <br>
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado. 

# 11 - Manejo de ficheros
**EJERCICIO:** <br>
Desarrolla un programa capaz de crear un archivo que se llame como tu usuario
de GitHub y tenga la extension .txt
Añade varias lineas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programacion favorito.
Imprime el contenido.
Borra el fichero.

**DIFICULTAD EXTRA (opcional):** <br>
Desarrolla un programa de gestion de ventas que almacena sus datos en un archivo .txt.
- Cada producto se guarda en una linea del archivo de la siguiente manera:
    [nombre_producto], [cantidad_vendida], [precio]
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
actualizar, eliminar productor y salir.
- Tambien debe poseer opciones para calcular la venta total y por producto.
- La opcion salir borra el .txt.

# 12 - JSON Y XML
IMPORTANTE: Solo debes subir el fichero de codigo como parte del ejercicio
**EJERCICIO:** <br>
desarrolla un programa capaz de crear un archivo XML y JSON que guarde los siguientes
datos (haciendo uso de la sintaxsis correcta en cada caso):
- Nombre
- Edad
- Fecha de nacimiento
- Listado de lenguajes de programacion
Muestra el contenido de los archivos.
Borra los archivos.

**DIFICULTAD EXTRA (opcional):** <br>
Utilizando la logica de creacion de los archivos anteriores, crea un programa capaz
de leer y transformar un una misma clase custom de tu lenguaje los datos
almacenados en el XML y en el JSON.
Borra los archivos.