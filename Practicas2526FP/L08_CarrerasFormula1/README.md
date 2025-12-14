# Proyecto L08_CarrerasFormula1

### Condiciones Iniciales:
Se dispone de una determinada cantidad de datos de telemetría y rendimiento de los vehículos que participan en carreras de formula 1, entre los que se encuentran los nombres de los pilotos que los pilotan y las respectivas escuderías.  
A continuación se solicitan una serie de ejercicios para realizar estudios comparativos. 
Se facilita una carpeta **data** con el fichero denominado ``f1.csv`` con datos medidos en distintas carreras. Ábralo para ver su estructura. 
La primera línea del fichero tiene el siguiente aspecto:
```  
Fernando Alonso;Aston Martin;21-11-22;25;330.1;30.5;-1;Abu Dhabi;[31.254/ 31.567/ 31.789/ 32.045/ -/ -];15.23;no
```
Lo que indica que Fernando Alonso, piloto de la escudería Aston Martin, participó en una carrera en Abu Dhabi que 
tuvo lugar el 21 de noviembre de 2022. La temperatura mínima que el sensor del coche pudo recoger fue de 
25 ºC y la velocidad máxima que alcanzó en toda la carrera fue de 330.1 km/h. Fernando no pudo acabar esa 
carrera porque tuvo un accidente. Los tiempos de sus mejores vueltas hasta el momento del accidente fueron 
31.254, 31.567, 31.789 y 32.045. El tiempo total que estuvo parado en boxes fue de 15.23 segundos, y no se 
bebió toda el agua disponible. 

Cree una carpeta **src** para incluir los siguientes módulos Python:

**f1.py** en el que implemente las funciones que se indican a continuación.

**f1_test.py** en el que incluirá las sentencias necesarias para ir probando las funciones a medida que las implemente.

 **Importante**: Los ejercicios suman un total de **9 puntos**, obtendrá los **10 puntos** si realiza adecuadamente los correspondientes tests. 

### Ejercicio 1
Implemente en ``f1.py`` el siguiente tipo de dato:

````
Carrera = NamedTuple("Carrera", [('nombre',str),('escudería',str),('fecha_carrera',date),('temperatura_min',int),('vel_max',float),('duración',float),('posición_final',int),('ciudad',str),('top_6_vueltas',list[int|float]),('tiempo_boxes',float),('nivel_liquido',bool)])

````
Cada campo tiene el siguiente significado:
```
Carrera:
• nombre: nombre del piloto, de tipo str. 
• escuderia: nombre de la escudería en la que corre el piloto, de tipo str. 
• fecha_carrera: fecha en la que se celebró la carrera, de tipo date. 
• temperatura_min: temperatura mínima que ha medido el sensor colocado en el frontal del monoplaza,de tipo int.
• vel_max: velocidad máxima alcanzada por el piloto en la carrera, de tipo float. 
• duracion: duración total en minutos que el piloto tardó en completar la carrera. Si el piloto no pudo terminar la carrera, este valor indica el tiempo que el piloto estuvo corriendo antes hast abandonar la carrera, de tipo float. 
• posición_final: puesto final en que terminó el piloto. Si el piloto no ha podido completar la carrera, este campo toma el valor -1, de tipo int.
• ciudad: nombre de la ciudad en la que se encuentra el circuito, de tipo str. 
• top_6_vueltas: lista con la duración en segundos de los tiempos que el piloto ha conseguido en sus 6 mejores vueltas. Si debido a abandono el piloto no ha podido completar ni tan siquiera 6 vueltas, habrá elementos que aparecerán con el valor ‘-‘. 
• tiempo_boxes: duración total en segundos del tiempo que el piloto estuvo ha estado parado en boxes en distintas intervenciones de sustitución de elementos o ajustes menores, de tipo float.
• nivel_liquido: valor que indica si el piloto se ha bebido toda el agua disponible en el tanque situado a sus espaldas (1 = se considera cierto, no = se considera falso), de tipo bool.
```
### Ejercicio 2
Defina una función ``lee_carreras`` que reciba como parámetro el nombre de un fichero con la estructura de ``f1.csv`` y devuelva una lista de tuplas de tipo **Carrera** con los registros leídos del fichero.
 
 **Nota**: Preste especial atención a la lista: aquellos
valores en los que no haya resultado, es decir aquellos con el carácter “-“, deberán transformarse a 0. Esto quiere decir que si la cadena de texto es [31.254; 31.567; 31.789; 32.045; - ; -], el resultado de salida deberá ser una lista con los valores [31.254, 31.567, 31.789, 32.045, 0, 0]. Observe que los ceros son de tipo int, mientras que el resto de valores son float, por lo que el tipo de salida de la función que use para "parsear" será **list[int|float]** que indica que la lista puede tener valores enteros o reales. **(1 punto)**

``def lee_carreras(ruta_fichero:str)->list[Carrera]:``

Resultados esperados en el test:
```
test_lee_carreras
Total registros leídos: 45
Mostrando los dos primeros registros:
        Carrera(nombre='Fernando Alonso', escudería='Aston Martin', fecha_carrera=datetime.date(2022, 11, 21), temperatura_min=25, vel_max=330.1, duración=30.5, posición_final=-1, ciudad='Abu Dhabi', top_6_vueltas=[31.254, 31.567, 31.789, 32.045, 0, 0], tiempo_boxes=15.23, nivel_liquido=False)
        Carrera(nombre='Fernando Alonso', escudería='Aston Martin', fecha_carrera=datetime.date(2022, 12, 5), temperatura_min=28, vel_max=328.5, duración=123.86, posición_final=2, ciudad='Sao Paulo', top_6_vueltas=[30.976, 31.189, 31.435, 31.679, 31.827, 32.015], tiempo_boxes=12.87, nivel_liquido=False)
```
### Ejercicio 3 (se deja para casa o para el final del laboratorio)
Defina una función ``media_tiempo_boxes`` que reciba una lista de tuplas de tipo Carrera, una ciudad y una fecha (con valor por defecto **None**), y devuelva la media de tiempo que los pilotos han pasado en boxes en la fecha y ciudad seleccionadas. Si la fecha es None, se sumarán todos los tiempos de la ciudad sin tener en cuenta la fecha. Por otro lado, si no ha habido carreras en la fecha y ciudad seleccionada, la media debe ser 0. **(1 punto)**
 
 ``
 def media_tiempo_boxes(carreras:list[Carrera], fecha:date|None=None)->int|float:
 ``
 
Resultados esperados en el test:
```
test_media_tiempo_boxes
La media de tiempo en boxes el None fue de 12.460666666666661 segundos.

test_media_tiempo_boxes
La media de tiempo en boxes el 2023-05-07 fue de 6.536 segundos.

test_media_tiempo_boxes
La media de tiempo en boxes el 1905-01-01 fue de 0 segundos.
```
### Ejercicio 4 (se deja para casa o para el final del laboratorio)
Defina una función ``pilotos_menor_tiempo_medio_vueltas_top`` que reciba una lista de tuplas de tipo Carrera y un número entero n, y devuelva una lista de tuplas (nombre, fecha) con los n nombres y fechas de carrera de los pilotos cuya media de tiempo en sus 6 vueltas top sea menor. No se tendrán en cuenta los datos de aquellas carreras que no han podido completar las 6 vueltas. **(1.5 puntos)**

``def pilotos_menor_tiempo_medio_vueltas_top(carreras:list[Carrera], n:int)->list[tuple[str,date]]: ``

 Resultados esperados en el test:
```
test_pilotos_menor_tiempo_medio_vueltas_top
Los 4 pilotos con menor tiempo medio son [('Lewis Hamilton', datetime.date(2023, 5, 21)), ('Max Verstappen', datetime.date(2023, 5, 21)), ('Fernando Alonso', datetime.date(2023, 5, 21)), ('Carlos Sainz', datetime.date(2023, 5, 21))].
```
### Ejercicio 5
Defina una función ``ratio_tiempo_boxes_total`` que reciba una lista de tuplas de tipo Carrera, y devuelva una lista de tuplas (nombre, fecha, ratio) con el nombre del piloto, la fecha de la carrera y la ratio entre su tiempo en boxes con respecto al total de tiempo en boxes de todos los pilotos que han participado **ese día en la carrera**. La lista de tuplas resultante deberá estar ordenada de mayor a menor ratio. **(2 puntos)**

 **Nota**: Use las funciones **round o format** en el test para que ratio aparezca formateada con 3 decimales. La fecha puede visualicarla como una string, si previamente le ha aplicado strftime.

``def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date,float]]:``

Resultados esperados en el test (en total se visualizarían 45 registros, pero aquí sólo se muestran los 3 primeros y los 3 últimos):
``` 
test_ratio_tiempo_boxes_total
(Fernando Alonso, 2023-05-21, 0.23573952549217564)
(Carlos Sainz, 2022-11-21, 0.22956815304543535)
(Fernando Alonso, 2023-05-07, 0.22460220318237453)
...
(Max Verstappen, 2023-06-04, 0.1807603571070318)
(Max Verstappen, 2023-05-21, 0.17415446744068652)
(Lewis Hamilton, 2022-11-21, 0.16247010831340555)
```

### Ejercicio 6
Defina una función ``mejor_escuderia_año`` que reciba una lista de tuplas de tipo Carrera y un año a, y devuelve la escudería que más victorias haya conseguido en el año a. Se considera victoria cuando algún piloto de la escudería queda en el primer puesto. **(1.5 puntos)**

``def mejor_escuderia_año(carreras:list[Carrera], año:int)->str:``

Resultados esperados en el test
```
test_mejor_escuderia_año
La mejor escudería en el año 2022 ha sido Mercedes.
```

### Ejercicio 7
Defina una función ``puntos_piloto_años`` que reciba una lista de tuplas de tipo Carrera, y devuelve un diccionario que asocia cada piloto (clave) con una lista de tuplas con los años y los puntos totales obtenidos en dicho año (valores). La lista de tuplas deberá estar ordenada por año. 

Para calcular los puntos obtenidos en cada carrera, debe tener en cuenta que solamente obtienen puntos aquellos pilotos que quedan en las 3 primeras posiciones. Si el puesto es el primero, los puntos serían 50, el segundo puesto son 25 y el tercero 10. Para este cálculo de puntos se le aconseja utilizar una función auxiliar que, dada una posición devuelva los puntos que correspondan. **(2 puntos)**

``def puntos_piloto_años(carreras:list[Carrera])->dict[str,list[tuple[int,int]]]``

Resultados esperados en el test:
```
test_puntos_piloto_años
Puntos por año de cada uno de los pilotos:
        Fernando Alonso --> [(2022, 25), (2023, 85)]
        Lewis Hamilton --> [(2022, 125), (2023, 175)]
        Max Verstappen --> [(2022, 85), (2023, 145)]
        Charles Leclerc --> [(2022, 10), (2023, 70)]
        Carlos Sainz --> [(2022, 0), (2023, 25)]
```
