# Ejercicio de laboratorio: Rios

### Condiciones iniciales
Se considera la siguiente lista de ríos:
```python
rios = [Rio("Amazonas", 7062, "América del Sur"), Rio("Nilo", 6853, "África"),
        Rio("Yangtsé", 6300, "Asia"), Rio("Misisipi", 6275, "América del Norte"),
        Rio("Amarillo", 5464, "Asia"), Rio("Mekong", 4880, "Asia"),
        Rio("Congo", 4700, "África"), Rio("Danubio", 2850, "Europa")]
```
y el siguiente tipo:
```python
from typing import NamedTuple

Rio = Namedtuple("Rio", [("nombre",str),("longitud",int),("continente",str)])
```

En la carpeta **src** debe crear los dos módulos: ``rios.py`` y ``test_rios.py``

En el módulo **rios.py** debe implementar los tipos y las funciones que se piden en los siguientes los ejercicios y a medida que los realice, implemente también en **test_rios.py** los oportunos test para obtener los resultados esperados.

### Ejercicio 0:
Implemente el tipo Rio.

### Ejercicio 1:

Implemente una función que cargue y devuelva la lista de rios que se proporciona en este enunciado. 
```python
def carga_rios()->list[Rio]:

```

Se proporciona un test inicial para ir completando a **medida que implementa los siguientes ejercicios**

```Python
from rios import *

def test_carga_rios(rios:list[Rio])->None:
  print("\n1. Test_carga_rios")
 ....


if __name__=='__main__':
  rios=carga_rios()
  test_carga_rios(rios)
````

Resultados esperados:
```
1. Test_carga_rios
Rio(nombre='Amazonas', longitud=7062, continente='América del Sur')  
Rio(nombre='Nilo', longitud=6853, continente='África')
Rio(nombre='Yangtsé', longitud=6300, continente='Asia')
Rio(nombre='Misisipi', longitud=6275, continente='América del Norte')
Rio(nombre='Amarillo', longitud=5464, continente='Asia')
Rio(nombre='Mekong', longitud=4880, continente='Asia')
Rio(nombre='Congo', longitud=4700, continente='África')
Rio(nombre='Danubio', longitud=2850, continente='Europa')
```

### Ejercicio 2:

Implemente una función que recibiendo una ``lista de rios`` y ``un nombre de continente``, devuelva una lista de rios del continente dado.

```Python
def filtra_rios_de_continente(rios:list[Rio],continente:str)->list[Rio]:
```
Resultados esperados:
````
2. test_filtra_rios_de_continente
Para el continente asia -->[Rio(nombre='Yangtsé', longitud=6300, continente='Asia'), Rio(nombre='Amarillo', longitud=5464, continente='Asia'), Rio(nombre='Mekong', longitud=4880, continente='Asia')]
Para el continente África -->[Rio(nombre='Nilo', longitud=6853, continente='África'), Rio(nombre='Congo', longitud=4700, continente='África')]
````

### Ejercicio 3:

Implemente una función que recibiendo ``una lista de rios``, devuelva una lista de tuplas con el nombre del continente y nombre del rio.
La lista devuelta debe estar ordenada por el nombre de los rios.

```Python
def obtener_continentes_y_rios(rios:list[Rio])->list[tuple[str,str]]:
```
Resultados esperados:
````
3. test_obtener_continentes_y_rios
('Asia', 'Amarillo')
('América del Sur', 'Amazonas')
('África', 'Congo')
('Europa', 'Danubio')
('Asia', 'Mekong')
('América del Norte', 'Misisipi')
('África', 'Nilo')
('Asia', 'Yangtsé')
````

### Ejercicio 4:

Implemente una función que recibiendo ``una lista de rios`` devuelva cuantos continentes hay con rios de 6.300 kms o más de longitud.

```Python
def contar_diferentes_continentes(rios:list[Rio])->int:
```
Resultados esperados:
````
4. test_contar_diferentes_continentes
Hay 3 continentes diferentes con rios de más de 6.300 kms
````

### Ejercicio 5:

Implemente una función que recibiendo ``una lista de rios`` y un ``conjunto con nombres de continentes``, devuelva la suma de las longitudes de los rios de dichos continentes

```Python
def suma_longitudes(rios:list[Rio],continentes:set[str])->int:
```
Resultados esperados:
````
5. test_suma_longitudes
La suma de las longitudes de los rios de {'Asia', 'Europa'} es 19494
````

### Ejercicio 6:

Implemente una función que recibiendo ``una lista de rios`` y un ``conjunto con nombres de continentes``, devuelva el nombre del rio cuyo nombre es el más corto.

```Python
def rio_con_nombre_más_corto(rios:list[Rio],continentes:set[str])->str:
```
Resultados esperados:
````
6. test_rio_con_nombre_más_corto
El rio con el nombre más corto de {'Europa', 'Asia', 'América del Sur'} es Mekong
````

### Ejercicio 7:

Implemente una función que recibiendo ``una lista de rios`` y un parámetro de tipo ``bool`` que si toma el valor ``True`` devuelva los nombre de los tres rios de mayor longitud, mientra que si vale ``False``devuelva los de menor longitud

```Python
def nombres_3_rios_longitud(rios:list[Rio],más_largos:bool)->list[str]:
```
Resultados esperados:
````
7. test_nombres_3_rios_longitud
Los nombres de los tres rios de mayor longitud son: ['Amazonas', 'Nilo', 'Yangtsé']
Los nombres de los tres rios de menor longitud son: ['Danubio', 'Congo', 'Mekong']
````