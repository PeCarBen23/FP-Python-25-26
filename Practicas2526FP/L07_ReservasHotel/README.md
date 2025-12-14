# Proyecto L06_ReservasHotel

### Condiciones Iniciales:
Se facilita una carpeta **data** con el fichero denominado ``reservas.csv`` con datos sobre reservas hoteleras. Ábralo para ver su estructura. 

Cree una carpeta **src** para incluir los siguientes módulos Python:

**reservas.py** en el que implemente las funciones que se indican a continuación.

**test_reservas.py** en el que incluirá las sentencias necesarias para ir probando las funciones a medida que las implemente.

### Ejercicio 1
Defina en ``reservas.py`` los tipos **FechasEstancia** y  **Reserva** con los siguientes campos:
```
FechasEstancia   --> "fecha_entrada", "fecha_salida" con el siguiente significado y tipo:

*fecha_entrada: fecha de entrada en el hotel de tipo date.
*fecha_salidas: fecha de salida del hotel de tipo date. 
                    
Reserva --> 'nombre', 'dni', 'fechas', 'tipo_habitación', 'num_personas', 'precio_noche', 'servicios_adicionales', con el siguiente significado y tipo:

* nombre: nombre a quien está hecha la reserva, de tipo str
* dni: dni a quien está hecha la reserva, de tipo str
* fechas: tupla que contiene la fecha de entrada y de salida, de tipo FechasEstancia. Vea los resultados esperados en el test de lectura 
* tipo_habitación: tipo de habitación para la que se ha hecho la reserva, de tipo str
* num_personas: número de personas que se alojarán en la habitación, de tipo int
* precio_noche: precio por el uso de la habitación durante una noche, de tipo float
* servicios_adicionales: lista con servicios adicionales, de tipo lista de str. En caso de que no se hayan contratado servicios adicionales debe devolver una lista vacía (vea el segundo y tercer registro del test lee_reservas).
```
Se facilitan los respectivos tipos:

``
Fechas_Estancia = NamedTuple("Fechas_Estancias",
                     [("fecha_entrada", date),
                      ("fecha_salida", date)])
``

``
Reserva = NamedTuple("Reserva",
                     [("nombre", str),
                      ("dni", str),
                      ("fechas", Fechas_Estancia),
                      ("tipo_habitacion", str),
                      ("num_personas", int),
                      ("precio_noche", float),
                      ("servicios_adicionales", list[str]|None)
                    ])
``

### Ejercicio 2
Defina una función ``lee_reservas`` que reciba como parámetro el nombre de un fichero con la estructura de ``reservas.csv`` y devuelva una lista de tuplas de tipo **Reserva** con los registros leídos del fichero

**Nota**: Si ha observado cada registro del fichero tiene 8 campos, pero el tipo Reserva tiene 7, debido a que tiene que gestionar adecuadamente la lectura de las ``fechas de entrada y salida``. Es decir, debe leerlas como cadenas pero cuando construya la tupla ``Reserva`` deberán ser una sóla tupla de tipo ``Fechas_Estancia`` que agrupe las dos fechas. Vea los resultados esperados en el test de lectura.

Resultados esperados en el test:
```
test_lee_reservas
Total reservas: 496
Las tres primeras:
Reserva(nombre='Ana Fernández', dni='98762912S', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 1, 2), fecha_salida=datetime.date(2022, 1, 6)), tipo_habitacion='Suite', num_personas=4, precio_noche=202.97, servicios_adicionales=['Parking', 'Gimnasio', 'Spa'])
Reserva(nombre='María Fernández', dni='25061289Y', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 1, 1), fecha_salida=datetime.date(2022, 1, 3)), tipo_habitacion='Familiar', num_personas=4, precio_noche=83.77, servicios_adicionales=[])
Reserva(nombre='Laura López', dni='13728274B', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 1, 2), fecha_salida=datetime.date(2022, 1, 10)), tipo_habitacion='Estandar', num_personas=1, precio_noche=87.58, servicios_adicionales=[])
```

### Ejercicio 3
Defina una función ``total_facturado`` que reciba una lista de tuplas de tipo Reserva, una fecha inicial y una fecha final que pueden tomar el valor **None**, y devuelve el total facturado entre todas las reservas cuya fecha de entrada esté comprendida entre esas fechas dadas como parámetros.

**Nota 1:** La cantidad facturada correspondiente a una reserva se calcula multiplicando el número de días totales de la reserva por el precio por noche. 

**Nota 2:** Si la fecha inicial es **None** se hace el cálculo sin limitar la fecha mínima de las reservas. Si la fecha final es **None** se hace el cálculo sin limitar la fecha máxima de las reservas.

Resultados esperados en el test:
```
test_total_facturado
Total facturado entre None y None: 244275.89000000028

test_total_facturado
Total facturado entre 2022-02-01 y 2022-02-28: 19098.12

test_total_facturado
Total facturado entre 2022-02-01 y None: 221532.13000000015
```
### Ejercicio 4
Defina una función ``servicios_adicionales`` que reciba como parámetro una lista de tuplas de tipo Reserva  y devuelva una lista ordenada alfabéticamente de los distintos servicios adicionales

Resultados esperados en el test:
```
test_servicios_adicionales
Los distintos servicios adicionales son: ['Gimnasio', 'Parking', 'Piscina', 'Spa']
```
### Ejercicio 5
Defina una función ``reservas_más_largas`` que reciba una lista de tuplas de tipo Reserva y un entero n, y devuelve las n tuplas (nombre, fecha_entrada) más largas. Es decir, con mayor número de días entre la fecha de entrada y la fecha de salida.

Resultados esperados en el test:
```
test_reservas_mas_largas
Para n=3 son: [('Laura López', datetime.date(2022, 1, 2)), ('Sofía García', datetime.date(2022, 1, 4)), ('Miguel Sánchez', datetime.date(2022, 1, 2))]
```
### Ejercicio 6
Defina una función ``dni_por_tipo`` que reciba como parámetro una lista de tuplas de tipo Reserva, un servicio adicional  y devuelva un diccionario con los dni's que se han alojado en cada tipo de habitación y que la reserva incluya el servicio dado.

Resultados esperados en el test

**(Observe que cada pareja clave-valor del diccionario se está mostrando una debajo de otra, por lo que debe recorrer dicho diccionario)**
```
Los distintos dni's con servicio adicional de Piscina, por tipo de habitación son:
test_dni_por_tipo
Los distintos dni's con servicio adicional de Piscina, por tipo de habitación son:
Suite --> {'27595453F', '26889506E', '36283527S', '52801249B', '88692655D', '48337470A', '04324992A', '71494621H', '63910637P', '51199390X', '13728274B', '52230529J', '65680492J', '89565833S', '72264876A', '76665848V', '98513684S', '96641529Z'}  
Familiar --> {'23053985G', '26889506E', '36283527S', '02325669R', '04324992A', '76188479J', '12527462Y', '52103097R', '65213761K', '98831781E', '04847825T', '60489278Z', '03143754E'}
Deluxe --> {'22080652P', '48337470A', '93407846Q', '33150540L', '96641529Z', '67017895N', '03360550C', '65680492J', '63550791C', '52230529J', '81378994A', '34452687K', '73575244S', '94336582N', '43257294K', '04812247A', '38645040A', '04264926J', 
'60489278Z', '10208905X'}
Doble --> {'27595453F', '15361035W', '22080652P', '13359010N', '36283527S', '25061289Y', '81312679C', '08437903P', '93141626K', '71970039A', '12527462Y', '20210823X', '63550791C', '98762912S', '04812247A'}
Estandar --> {'13359010N', '43257294K', '35963657Y', '07424130Y', '22881672F', '04264926J', '70563584K'}
```
### Ejercicio 7
Defina una función ``cliente_mayor_facturacion`` que reciba una lista de tuplas de tipo Reserva y un conjunto de servicios que puede tomar el valor por defecto **None**, y devuelve una tupla(dni, total_facturado) con el dni del cliente al que se le ha facturado más, junto con el total facturado, teniendo en cuenta sólo aquellas reservas en las que se haya contratado **alguno** de los servicios adicionales indicados.
Si el conjunto de servicios toma el valor None  se procesarán todas las reservas.


Resultados esperados en el test
```
test_cliente_mayor_facturacion
Para los servicios None el cliente es:('63550791C', 3893.2200000000003)

test_cliente_mayor_facturacion
Para los servicios {'Parking'} el cliente es:('71828448T', 3008.17)

test_cliente_mayor_facturacion
Para los servicios {'Parking', 'Spa'} el cliente es:('38747931S', 3216.0699999999997)
```

### Ejercicios para resolver con dos diccionarios
### Ejercicio 8
Defina una función ``promedios_dias_estancias_por_tipo`` que reciba una lista de tuplas de tipo Reserva y devuelva un diccionario con el promedio de días en que se reserva cada tipo de habitación.

Resultados esperados en el test
```
test_promedios_dias_estancias_por_tipo
{'Suite': 2.9320388349514563, 'Familiar': 3.019607843137255, 'Estandar': 2.875, 'Doble': 2.966292134831461, 'Deluxe': 3.1403508771929824}
```
## Ejercicio 9
Defina una función ``reserva_más_barata_por_numero_personas`` que reciba una lista de tuplas de tipo Reserva y un conjunto de servicios adicionales, que por defecto puede valer **None**, y que devuelva un diccionario con la reserva con precio por noche más barata para cada número de personas en las que se han contratado alguno de los servicios dados como parámetro, salvo que se omitan, en cuyo caso se considerarán todas las reservas. 

Resultados esperados en el test
```
test_reserva_más_barata_por_número_personas
Para los servicios None
4 --> Reserva(nombre='María Martínez', dni='72264876A', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 10, 30), fecha_salida=datetime.date(2022, 11, 4)), tipo_habitacion='Deluxe', num_personas=4, precio_noche=82.51, servicios_adicionales=['Gimnasio', 'Spa'])
1 --> Reserva(nombre='Sofía Martín', dni='93141626K', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 1, 20), fecha_salida=datetime.date(2022, 1, 21)), tipo_habitacion='Suite', num_personas=1, precio_noche=80.42, servicios_adicionales=[])
2 --> Reserva(nombre='Laura Martínez', dni='48337470A', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 3, 4), fecha_salida=datetime.date(2022, 3, 5)), tipo_habitacion='Deluxe', num_personas=2, precio_noche=80.86, servicios_adicionales=[])
3 --> Reserva(nombre='Sofía Sánchez', dni='25460473W', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 3, 15), fecha_salida=datetime.date(2022, 3, 20)), tipo_habitacion='Familiar', num_personas=3, precio_noche=80.03, servicios_adicionales=['Parking', 'Gimnasio', 'Spa'])

test_reserva_más_barata_por_número_personas
Para los servicios {'Gimnasio', 'Spa'}
4 --> Reserva(nombre='María Martínez', dni='72264876A', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 10, 30), fecha_salida=datetime.date(2022, 11, 4)), tipo_habitacion='Deluxe', num_personas=4, precio_noche=82.51, servicios_adicionales=['Gimnasio', 'Spa'])
1 --> Reserva(nombre='Laura Sánchez', dni='03143754E', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 1, 13), fecha_salida=datetime.date(2022, 1, 16)), tipo_habitacion='Deluxe', num_personas=1, precio_noche=81.77, servicios_adicionales=['Gimnasio', 'Spa', 'Parking'])
2 --> Reserva(nombre='Sofía Fernández', dni='76665848V', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 11, 26), fecha_salida=datetime.date(2022, 11, 29)), tipo_habitacion='Suite', num_personas=2, precio_noche=81.54, servicios_adicionales=['Parking', 'Spa'])
3 --> Reserva(nombre='Sofía Sánchez', dni='25460473W', fechas=Fechas_Estancias(fecha_entrada=datetime.date(2022, 3, 15), fecha_salida=datetime.date(2022, 3, 20)), tipo_habitacion='Familiar', num_personas=3, precio_noche=80.03, servicios_adicionales=['Parking', 'Gimnasio', 'Spa'])
```
### Ejercicio 10
Defina una función ``reserva_mas_cara_por_mes`` que reciba una lista de tuplas de tipo Reserva y devuelva un diccionario que a cada **número del mes de la fecha de entrada** le haga corresponder una tupla con el dni, el nombre del cliente, y el total facturado del cliente con mayor total facturado para el mes correspondiente a la clave.

Resultados esperados en el test
```
test_reserva_más_cara_por_mes
1 --> ('03360550C', 'Miguel Sánchez', 1483.3799999999999)
2 --> ('71193098W', 'Miguel Fernández', 1248.8500000000001)
3 --> ('02325669R', 'Luis Gómez', 1154.4499999999998)
4 --> ('27595453F', 'Sofía López', 1181.05)
5 --> ('63910637P', 'Ana García', 1199.6)
6 --> ('38747931S', 'Javier Fernández', 1216.7)
7 --> ('63550791C', 'Javier Martínez', 1140.9)
8 --> ('71828448T', 'Carmen García', 1212.1)
9 --> ('94336582N', 'Miguel González', 944.95)
10 --> ('26889506E', 'Luis López', 1241.1)
11 --> ('10208905X', 'Miguel García', 1055.6)
12 --> ('20210823X', 'María González', 1238.0500000000002)
```

## Ejercicio 11
Defina una función ``clientes_por_servicio`` que reciba una lista de tuplas de tipo Reserva, un número entero "n" y un tipo de habitación que puede tomar por defecto el valor **None** y devuelva un diccionario que a cada servicio adicional le haga corresponder una lista de tuplas con el dni, el nombre del cliente y el precio noche de las reservas, **ordenada de menor a mayor precio por noche**, de los "n" clientes que han contratado el servicio adicional de que se trate y se han alojado en el tipo de habitación dado, salvo que tome el valor **None**, en cuyo caso se tendrá en cuenta todo tipo de habitación. 

Resultados esperados en el test
```
test_clientes_por_servicio
Para n=3 y tipo None:
Parking --> [('25460473W', 'Sofía Sánchez', 80.03), ('76665848V', 'Sofía Fernández', 81.54), ('03143754E', 'Laura Sánchez', 81.77)]
Gimnasio --> [('25460473W', 'Sofía Sánchez', 80.03), ('03143754E', 'Laura Sánchez', 81.77), ('72264876A', 'María Martínez', 82.51)]
Spa --> [('25460473W', 'Sofía Sánchez', 80.03), ('76665848V', 'Sofía Fernández', 81.54), ('03143754E', 'Laura Sánchez', 81.77)]
Piscina --> [('26889506E', 'Luis López', 82.94), ('22080652P', 'Luis Martínez', 91.35), ('02325669R', 'Luis Gómez', 94.95)]

test_clientes_por_servicio
Para n=4 y tipo Doble:
Parking --> [('22080652P', 'Luis Martínez', 91.35), ('93141626K', 'Sofía Martín', 101.53), ('27595453F', 'Sofía López', 107.59), ('62911458H', 'María Pérez', 113.66)]
Spa --> [('22080652P', 'Luis Martínez', 91.35), ('00967117J', 'Juan López', 96.16), ('23053985G', 'María López', 112.95), ('62911458H', 'María Pérez', 113.66)]
Gimnasio --> [('22080652P', 'Luis Martínez', 91.35), ('00967117J', 'Juan López', 96.16), ('15542641T', 'Miguel Martínez', 102.1), ('27595453F', 'Sofía López', 107.59)]
Piscina --> [('22080652P', 'Luis Martínez', 91.35), ('93141626K', 'Sofía Martín', 101.53), ('27595453F', 'Sofía López', 107.59), ('04812247A', 'Carmen Sánchez', 117.65)]
```
