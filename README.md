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

# 13 - Pruebas unitarias
**EJERCICIO:** <br>
Crea una funcion que se encargue de sumar dos numeros y retorne su resultado.
Crea un test, utilizando las herramientas de tu lenguaje, que sea capaz de
determinar si esa funcion se ejecuta correctamente.

**DIFICULTAD EXTRA (opcional):** <br>
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre"
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de programacion"]
Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducidos son correctos.

# 14 - Fechas
**EJERCICIO:** <br>
Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
- Una primera que represente la fecha (dia, mes, año, hora, minuto, segundo) actual.
- Una segunda que represente tu fecha de nacimiento (tu puedes inventar la hora).
Calcula cuantos años han transcurrido entre ambas fechas.

**DIFICULTAD EXTRA (opcional):** <br>
Utilizando la fecha de tu cumpleaños, formateala y muestra su resultadao de 10
maneras diferentes. Por ejemplo:
- Dia, mes y año
- Hora, minuto y segundo
- Dia de año
- Dia de la semana
- Nombre del mes
- (lo que se te ocurra)

# 15 - Asincronia
**EJERCICIO:** <br>
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera asincrona una funcion
que tardara en finalizar un numero concreto de segundos parametrizables. Tambien debes
poder asignarle un nombre.
La funcion imprime su nombre, cuando empieza, el tiempo que durara su ejecucion y cuando finaliza 

**DIFICULTAD EXTRA (opcional):** <br>
Utilizando el concepto de asincronia y la funcion anterior, crea el siguiente programa que ejecuta
en este orden:
- Una funcion C que dura 3 segundos.
- Una funcion B que dura 2 segundos.
- Una funcion A que dura 1 segundo.
- Una funcion D que dura 1 segundo.
- La funcion D comienza su ejecucion cuando las 3 anteriores han finalizado.

# 16 - Expresiones regulares
**EJERCICIO:** <br>
Utilizando tu lenguaje, explora el concepto de expresiones regulares, creando una que sea
capaz de encontrar y extraer todos los numeros de un texto.

**DIFICULTAD EXTRA (opcional):** <br>
Crea 3 expreisones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un numero de telefono.
- Validar una url.

# 17 - Iteraciones
**EJERCICIO:** <br>
Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
numeros del 1 al 10 mediante iteracion.

**DIFICULTAD EXTRA (opcional):** <br>
Escribe el mayor numero de mecanismos que posea tu lenguaje
para iterar valores. Eres capaz de utilizar 5? y 10?

# 18 - Conjuntos
**EJERCICIO:** <br>
Utilizando tu lenguaje, crea un conjunto de datos y realiza las siguientes operaciones.
- Añade un elemento al final.
- Añade un elemento al principio.
- Añade varios elementos en bloque al final.
- Añade varios elementos en bloque en una posicion especifica.
- Elimina un elemento en una posicion especifica.
- Actualiza un valor en una posicion especifica.
- Comprueba si un elemento se encuentra en el conjunto.
- Elimina todo el contenido del conjunto.

**DIFICULTAD EXTRA (opcional):** <br>
Muestra un ejemplo de las siguientes operaciones con conjuntos:
- Union.
- Interseccion.
- Diferencia.
- Diferencia simetrica.

# 19 - Enumeraciones
**EJERCICIO:** <br>
Utilizando tu lenguaje, explora la definicion del tipo de dato que siva
para definir enumeraciones (Enum).
Crea un Enum que represente los dias de la semana del lunes al domingo,
en ese orden. Con ese enumerado, crea una operación que muestre
el nombre del dia de la semana dependiendo del numero entero
utilizado (del 1 al 7)


**DIFICULTAD EXTRA (opcional):** <br>
Crea un pequeño sistema de gestion del estado de pedidos.
Implementa una clase que defina un pedido con las siguientes caracteristicas:
- El pedido tiene un identificador y un estado.
- El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
- Implementa las funciones que sirvan para modificar el estado:
    - Pedido enviado
    - Pedido cancelado
    - Pedido entregado
    (Establece una logica, por ejemplo, no se puede entregar si no se ha enviado, etc..)
- Implementa una funcion para mostrar texto descriptivo segun el estado actual.
- Crea diferentes pedidos y muestra como se interactua con ellos.

# 20 - Peticiones HTTP
**EJERCICIO:** <br>
Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza una peticion, 
a la web que tu quieras, verifica que dicha peticion fue exitosa y muestra por
consola el contenido de la web.

**DIFICULTAD EXTRA (opcional):** <br>
Utilizando la PokeAPI (https://pokeapi.co), crea un programa por terminal
al que le puedas solicitar informacion de un Pokemon concreto utilizando su nombre o numero.
- Muestra el nombre, id, peso, altura y tipo(s) del Pokemon.
- Muestra el nombre de su cadena de evoluciones.
- Muestra los juegos en los que aparece.
- Controla posibles errores.

# 21 - Callbacks
**EJERCICIO:** <br>
Explora el concepto de callback en tu lenguaje creando un ejemplo simple,
que muestre su funcionamiento.

**DIFICULTAD EXTRA (opcional):** <br>
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estara formado por una funcion que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmacion, una de listo
y otra de entrega.
- Debe imprimir un confirmacion cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre procesos.
- Debe invocar a cada callback siguiendo un orden de procesado.
- Debe notificar que el plato esta listo o ha sido entregado.

# 22 - Funciones de orden superior
**EJERCICIO:** <br>
Explora el concepto de funciones de orden superior en tu lenguaje 
creando ejemplos simples (a tu elección) que muestren su funcionamiento.

**DIFICULTAD EXTRA (opcional):** <br>
Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
lista de calificaciones), utiliza funciones de orden superior para 
realizar las siguientes operaciones de procesamiento y análisis:
- Promedio calificaciones: Obtiene una lista de estudiantes por nombre
  y promedio de sus calificaciones.
- Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
  que tienen calificaciones con un 9 o más de promedio.
- Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
- Mayor calificación: Obtiene la calificación más alta de entre todas las
  de los alumnos.
- Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

# 23 - Patron de diseño: Singleton
**EJERCICIO:** <br>
Explora el patron de diseño "singleton" y muestra como crearlo con un ejemplo generico.

**DIFICULTAD EXTRA (opcional):** <br>
Utiliza el patron de diseño "singleton" para reprensentar una clase que haga
referencia a la sesion de usuario de una aplicacion ficticia.
La sesion debe permitir asignar un usuario (id, username, nombre y email).
recuperar los datos del usuario y borrar los datos de la sesion.

# 24 - Decoradores
**EJERCICIO:** <br>
Explora el concepto de "decorador" y muestra como crearlo como un ejemplo generico.

**DIFICULTAD EXTRA (opcional):** <br>
Crea un decorador que sea capaz de contabilizar cuantas veces se ha llamado
a una funcion y aplicalo a una funcion de tu eleccion.

# 25 - Logs
**EJERCICIO:** <br>
Explora el concepto de "logging" en tu lenguaje. Configuralo y muestra un ejemplo,
con cada nivel de "severidad" disponible.

**DIFICULTAD EXTRA (opcional):** <br>
Crea un programa ficticio de gestion de tareas que permita añadir, eliminar y listar
dichas tareas.
- Añadir: recibe el nombre y descripcion.
- Eliminar: por nombre de la tarea.
Implementa diferentes mensajes de log que muestren informacion segun la tarea ejecutada.
Utiliza el log para visualizar el tiempo de ejecucion de cada tarea.

# 26 - Solid SRP
**EJERCICIO:** <br>
Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

**DIFICULTAD EXTRA (opcional):** <br>
Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
manejar diferentes aspectos como el registro de libros, la gestión de usuarios
y el procesamiento de préstamos de libros.
Requisitos:
1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
información básica como título, autor y número de copias disponibles.
2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
información básica como nombre, número de identificación y correo electrónico.
3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
tomar prestados y devolver libros.
Instrucciones:
1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
los tres aspectos mencionados anteriormente (registro de libros, registro de
usuarios y procesamiento de préstamos).
2. Refactoriza el código: Separa las responsabilidades en diferentes clases
siguiendo el Principio de Responsabilidad Única.

# 27 - Solid OCP
**EJERCICIO:** <br>
Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

**DIFICULTAD EXTRA (opcional):** <br>
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.

# 28 - Solid LSP
**EJERCICIO:** <br>
Explora el `Principio SOLID de Sustitucion de Liskov(Liskov Substitution Principle, LSP)`
y crea un ejemplo simple donde se muester su funcionamiento de forma correcta e incorrecta.

**DIFICULTAD EXTRA (opcional):** <br>
Crea una jerarquia de vehiculos. Todos ellos deben poder acelerar y frenar, asi como cumplir el LSP.
Instrucciones:
1. Crea la clase vehiculo.
2. Añade tres subclases de vehiculo.
3. Implementa las operaciones `acelerar` y `frenar` como corresponda.
4. Desarrolla un codigo que compruebe que se cumple el LSP.

# 29 - Solid ISP
**EJERCICIO:** <br>
Explora el `Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)` 
y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.

**DIFICULTAD EXTRA (opcional):** <br>
Crea un gestor de impresoras.
Requisitos:
1. Algunas impresoras sólo imprimen en blanco y negro.
2. Otras sólo a color.
3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
2. Aplica el ISP a la implementación.
3. Desarrolla un código que compruebe que se cumple el principio.

# 30 - Solid DIP
**EJERCICIO:** <br>
Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
de forma correcta e incorrecta.

**DIFICULTAD EXTRA (opcional):** <br>
Crea un sistema de notificaciones.
Requisitos:
1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
2. El sistema de notificaciones no puede depender de las implementaciones específicas.
Instrucciones:
1. Crea la interfaz o clase abstracta.
2. Desarrolla las implementaciones específicas.
3. Crea el sistema de notificaciones usando el DIP.
4. Desarrolla un código que compruebe que se cumple el principio.
