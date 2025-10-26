# LAB-calificaciones
**Autor**: Toñi Reina **Revisores**: Alfonso Bengoa, Fermín Cruz, Mariano González  **Fecha última modificación**: 16/09/2025

Se pretende ayudar a los alumnos de Fundamentos de Programación a calcular su nota en la asignatura. Para 
lograrlo, el primer paso consiste en identificar las funciones necesarias y, posteriormente, agruparlas según 
su responsabilidad. Al analizar el problema, distinguimos dos grandes tipos de funciones. Por un lado, las 
funciones encargadas de realizar los cálculos (como obtener la nota de teoría de un cuatrimestre, calcular 
la nota del cuatrimestre completo o la de evaluación continua). Estas funciones implementan la lógica de negocio.
Por otro lado, se encuentran las funciones destinadas a gestionar la interacción con el usuario, es decir, la lectura de datos y la presentación de resultados.

La separación de estos dos tipos de funciones en distintos módulos —`calificaciones.py` para la lógica de negocio
 y `calificaciones_ui.py` para la interfaz de usuario— facilita el mantenimiento, la reutilización y la detección 
 de errores, ya que cada módulo cumple un rol bien definido.

Además, es fundamental probar las funciones implementadas. Separar las pruebas de la implementación es una buena
 práctica que permite verificar el correcto funcionamiento del código sin mezclarlo con la lógica de negocio o 
 la interfaz de usuario. Por ello, se requiere un tercer módulo, `calificaciones_test.py`, destinado 
 exclusivamente a las pruebas.

Crea, por tanto. tres módulos en el proyecto Python (`calificaciones.py`,`calificaciones_test.py` y `calificaciones_ui.py`) e implementa las funciones que se solicitan en los siguientes apartados. Separa la definición de las funciones, incluyéndolas en el módulo `calificaciones.py`, 
de la invocación para probar esas funciones, incluyéndolas en el módulo `calificaciones_test.py`.

#### Apartado a

Escribe una función en el módulo `calificaciones`  llamada `nota_teoria` que, dadas las notas de los dos exámenes teóricos de un cuatrimestre, permita calcular la nota que un alumno tiene en el bloque teórico de ese cuatrimestre. La nota se calcula como la media de las notas de ambos cuatrimestres. Una nota con valor None indica que el alumno no se ha presentado al examen, y se considerará como un cero.

_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los dos números que están antes de la flecha las notas del primer y segundo exámen teórico, respectivamente, y el valor situado a la derecha de la flecha la nota obtenida.
```
9.1, 7.2 ==> 8.15
4.0, 6.0 ==> 5.0
4.0, 3.0 ==> 3.5
None, 3.0 ==>1.5
9.0, None ==> 4.5
None, None ==> 0.0
```

#### Apartado b

Escribe una función en el módulo 'calificaciones' llamada `nota_cuatrimestre` que, dadas las notas del primer examen teórico, el segundo examen teórico, y la nota del exámen práctico, devuelva la nota obtenida en ese cuatrimestre. La nota del cuatrimestre, siempre que la media de los dos cuestionarios teóricos sea superior o igual a 4, se calcula como 0,15 * T1 + 0,15 * T2 + 0,7 * P, siendo  T1 y T2 las notas de los exámenes teóricos y P la nota del examen práctico. Si la media no es superior a 4, la nota del cuatrimestre es 0. Un valor None en una nota indica que el alumno no se ha presentado al examen, y se considerará como un cero.


_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los números situados a la izquierda de la flecha las notas del primer examen teórico, del segundo y del examen práctico, respectivamente. La nota obtenida es el número situado a la derecha de la flecha.
```
9.1, 7.2, 8.1 ==> 8.110000000000001
4.0, 6.0, 5.0 ==> 5.0
4.0, 3.0, None ==> 0
None, 3.0, None  ==>0
9.0, None, 4.5 ==> 4.5
9.0, None, None ==> 1.3499999999999999
None, None, None ==> 0
```

 
#### Apartado c

Escribe una función en el módulo 'calificaciones' llamada `nota_continua` que, dadas una tupla con las notas de los 4 exámenes teóricos del curso, y otra tupla con la nota de los 
dos exámenes prácticos, devuelva la nota obtenida por evaluación continua. La nota de la evaluación continua se calcula como la media de las notas de los dos cuatrimestres,
siempre que la nota de ambos cuatrimestres sea superior a 5. Si en alguno de los dos cuatrimestres la nota es inferior a 5, entonces la nota es el mínimo entre 4 y la nota media de los cuatrimestres. El valor None en una nota indica que el alumno no se ha presentado al examen, y se considerará como cero.

_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los números situados a la izquierda de la flecha las notas del primer examen teórico, del segundo y del examen práctico, respectivamente. La nota obtenida es el número situado a la derecha de la flecha.
```
    notas teoría:  9.6, 9.9, 10.0, 9.8 notas_práctico: 9.7, 9.5 ==> 9.6675
    notas teoría: 4.4, 4.9, 5.1, 4.7 notas_práctico: 4.6, 4.8 ==> 4.0
    notas teoría: 4.0, 6.0, 4.0, 3.0 notas_práctico: 5.0, None ==> 2.5
    notas teoría: 9.0, None, 4.0, 3.0 notas_práctico: 4.5, None ==> 2.25
    notas teoría: 9.0, 5.0, 4.0, None notas_práctico: 4.5, None ==> 2.25
```
 
#### Apartado d

Escribe una función en el módulo `calificaciones` llamada `genera_mensaje` que, dadas las notas del primer cuatrimestre, el segundo cuatrimestre y la nota final, devuelva una cadena con un mensaje para el estudiante en función de los resultados obtenidos.

Los mensajes a devolver deben ser los siguientes:

    - "¡Enhorabuena! Has aprobado la asignatura." si la nota final es superior o igual a 5.
    - "Debes recuperar el primer cuatrimestre." si la nota del primer cuatrimestre es inferior a 5 y la del segundo superior o igual a 5.
    - "Debes recuperar el segundo cuatrimestre." si la nota del segundo cuatrimestre es inferior a 5 y la del primero superior o igual a 5.
    - "Debes recuperar toda la asignatura." si las notas de ambos cuatrimestres son inferiores a 5.

_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los el mensaje resultado el situado después de la flecha
```
nota cuat 1=6, nota cuat 2=5, nota final=6 ==>¡Enhorabuena! Has aprobado la asignatura.
nota cuat 1=4, nota cuat 2=6, nota final=4 ==>Te debes presentar a convocatoria con el primer cuatrimestre.
nota cuat 1=7, nota cuat 2=3, nota final=4 ==>Te debes presentar a convocatoria con el segundo cuatrimestre.
nota cuat 1=4, nota cuat 2=3, nota final=3.5 ==>Te debes presentar a convocatoria con los dos cuatrimestres. 
```
#### Apartado e

Escribe una función en el módulo `calificaciones_ui` llamada `solicita_notas` que solicite por teclado el nombre de un estudiante, las notas de los 4 cuestionarios de teoría y las de los 2 exámenes
prácticos y devuelva una tupla con todos los datos leídos en tres campos estructurados de la siguiente forma: 
- el primer campo es una cadena con el nombre del estudiante, 
- el segundo campo es una lista con las 4 notas de los exámenes teóricos, y 
- el tercer campo es otra lista con las dos notas de los exámenes prácticos.  

Implementa una segunda función llamada `mostrar_notas` que tome como entrada una tupla con el formato anterior que contenga los datos leidos por teclado y los muestre por consola.
En el módulo `calificaciones_test.py` invoca a estas funciones para solicitar a un usuario sus notas, y mostrarle sus resultados por consola, de la siguiente forma:

```
Introduzca su nombre: Toñi
Introduzca la nota del examen teórico 1 (- si no se ha presentado):
6.5
Introduzca la nota del examen teórico 2 (- si no se ha presentado):
7.8
Introduzca la nota del examen teórico 3 (- si no se ha presentado):
5.6
Introduzca la nota del examen teórico 4 (- si no se ha presentado):
6.0
Introduzca la nota del examen práctico 1 (- si no se ha presentado):
6.1
Introduzca la nota del examen práctico 2 (- si no se ha presentado):
5.0
Tus notas del primer cuatrimestre son:
 teoria 7.15, práctica 6.1, cuatrimestre 6.414999999999999
Tus notas del segundo cuatrimestre son:
 teoria 5.8, práctica 5.0, cuatrimestre 5.24
Tu nota final de la asignatura es 5.8275
Mensaje: ¡Enhorabuena! Has aprobado la asignatura.
```

