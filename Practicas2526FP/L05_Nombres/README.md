## Fundamentos de Programación
# Ejercicio de laboratorio: Nombres
### Autor: José A. Troyano
---

En este proyecto trabajaremos con datos correspondientes a los nombres de las personas nacidas en España desde 2002 a 2017. Los datos están tomados del Instituto Nacional de Estadística, donde se pueden encontrar muchos datos interesantes principalmente sobre la demografía, economía y sociedad españolas. Representaremos la información de entrada mediante listas de tuplas, y a partir de esta estructura implementaremos una serie de funciones que nos permitirán realizar varios tipos de consultas y generar visualizaciones.


## Estructura de las carpetas del proyecto
Se le facilita un carpeta

* **/data**: Que contiene el dataset o fichero del proyecto
    * **frecuencias_nombres.csv**: Archivo con datos de nombres de personas.

Debe implementar la carpeta y módulos que se indica:
* **/src**: Contendrá los siguinetes módulos de Python que conforman el proyecto.
   * **nombres.py**: Contiene funciones para explotar los datos.
   * **nombres_test.py**: Contiene funciones de test para probar las funciones del módulo **nombres.py**. En este módulo está bloque de sentencias ``main``. 

Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada ocupa una línea y contiene cuatro informaciones sobre los nombres (año, nombre, frecuencia, genero). Estas son las  primeras líneas de un fichero de entrada: 

```
Año,Nombre,Frecuencia,Género
2002,ALEJANDRO,8020,Hombre
2002,PABLO,5799,Hombre
2002,DANIEL,5603,Hombre
2002,DAVID,5414,Hombre
```


Para almacenar estos datos en memoria, utilizaremos tuplas con nombre con la siguiente definición:

``
FrecuenciaNombre = NamedTuple('Frecuencia', [('año',int),('nombre',str),('frecuencia',int),('género',str)])
``

## Ejercicios a realizar


**1. leer_frecuencias_nombres**: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo FrecuenciaNombre con todos los datos del fichero.

_Resultado del test_:
```python
1. test_frecuencias_nombres'

Leídos 3505 registros
Mostrando los 3 primeros:
    [Registro(año=2002, nombre='ALEJANDRO', frecuencia=8020, genero='Hombre'), Registro(año=2002, nombre='PABLO', frecuencia=5799, genero='Hombre'), Registro(año=2002, nombre='DANIEL', frecuencia=5603, genero='Hombre')]

Mostrando los 3 últimos:
    [Registro(año=2017, nombre='NAIARA', frecuencia=330, genero='Mujer'), Registro(año=2017, nombre='NAHIA', frecuencia=322, genero='Mujer'), Registro(año=2017, nombre='ELISA', frecuencia=317, genero='Mujer')]
	
```
**2. filtrar_por_genero**: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve una lista de tuplas de tipo FrecuenciaNombre con los registros del género recibido como parámetro.

_Resultado del test_:
```python
2. test_filtrar_por_genero
Número de registros para hombre: 1752

2. test_filtrar_por_genero
Número de registros para Mujer: 1753
```
**3. calcular_nombres**: recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y devuelve un conjunto {str} con los nombres del género recibido como parámetro. El género puede ser 'Hombre', 'Mujer'.

**Nota** Como la función devuelve un conjunto que no tiene ordenación, en el test, en vez de visualizar el conjunto directamente ordenelo para mostrar los nombres en orden alfabetico.

_Resultado del test_:
```python
3. test_calcular_nombres
HOMBRE --> ['AARON', 'ABEL', 'ABRAHAM', 'ABRIL', 'ADAM', 'ADAN', 'ADRIA', 'ADRIAN', 'AGUSTIN', 'AIMAR']

3.test_calcular_nombres
MUJER --> ['ABRIL', 'ADARA', 'ADRIANA', 'AFRICA', 'AIDA', 'AINA', 'AINARA', 'AINHOA', 'AINOA', 'AITANA']
```
**4. calcular_top_nombres_de_año**: recibe una lista de tuplas de tipo FrecuenciaNombre, un año de tipo int, un número máximo de nombre a mostrar de tipo int y un género de tipo str, y devuelve una lista de tuplas (nombre, frecuencia) de tipo (str, int) con los nombres más frecuentes del año del género dado, ordenada de mayor a menor frecuencia.

_Resultado del test_:
```python

4.test_calcular_top_nombres_de_año
Año:2008 - Límite:4 - género: hombre -->[('DANIEL', 6580), ('ALEJANDRO', 6478), ('PABLO', 5911), ('DAVID', 5385)]

4.test_calcular_top_nombres_de_año
Año:2009 - Límite:7 - género: mujer -->[('LUCIA', 6847), ('PAULA', 6549), ('MARIA', 6113), ('SARA', 4417), ('DANIELA', 4279), ('CARLA', 3976), ('CLAUDIA', 3711)]
```

**5. calcular_nombres_ambos_generos**: recibe una lista de tuplas de tipo FrecuenciaNombre, y devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.

_Resultado del test_:
```python
5.test_calcular_nombres_ambos_generos
Nombre de ambos géneros: {'ABRIL'}
```

**6. calcular_promedio_frecuencia_nombre_años**: recibe una lista de tuplas de tipo FrecuenciaNombre, un nombre, un año inicial y un año final y calcula la frecuencia media del nombre dado como parámetro en el rango de años [año_inicial, año_final). Si no se puede calcular la media devuelve `None`.

_Resultado del test_:
```python
6.test_calcular_promedio_frecuencia_nombre_años
La frecuencia media del nombre Nerea entre 2005 y 2010 es: 2579.2
```

