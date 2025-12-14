# nombres.py
from typing import *
from typing import NamedTuple
import csv

#Trabajo Previo
# Definición de la tupla FrecuenciaNombre
FrecuenciaNombre = NamedTuple("FrecuenciaNombre", [
    ("año", int),
    ("nombre", str),
    ("frecuencia", int),
    ("genero", str)
])

def lee_nombres(ruta: str) -> List[FrecuenciaNombre]:
    # Lee el fichero CSV y devuelve una lista de tuplas FrecuenciaNombre
    res: List[FrecuenciaNombre] = []
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        next(lector)  # saltar la cabecera
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            res.append(FrecuenciaNombre(año, nombre, frecuencia, genero))
    return res

#1
def lee_nombres(ruta: str) -> List[FrecuenciaNombre]:
    # Crea una lista vacía para almacenar los registros leídos del fichero
    res: List[FrecuenciaNombre] = []
    
    # Abre el fichero CSV en modo lectura con codificación UTF-8
    with open(ruta, encoding="utf-8") as f:
        
        # Crea un lector CSV usando coma como delimitador
        lector = csv.reader(f, delimiter=",")
        
        # Salta la primera línea del fichero (cabecera)
        next(lector)
        
        # Recorre cada línea del fichero y convierte los datos a su tipo correspondiente
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            res.append(FrecuenciaNombre(año, nombre, frecuencia, genero))
    
    # Devuelve la lista completa de registros leídos
    return res


#2
def frecuencias_generos(ruta: str) -> Tuple[int, int]:
    # Lee los datos del fichero usando la función lee_nombres
    lista: List[FrecuenciaNombre] = lee_nombres(ruta)

    # Inicializa los contadores de hombres y mujeres
    hombres: int = 0
    mujeres: int = 0

    # Recorre todos los registros y cuenta según el valor del campo "genero"
    for fn in lista:
        if fn.genero.lower() == "hombre":
            hombres = hombres + 1
        elif fn.genero.lower() == "mujer":
            mujeres = mujeres + 1

    # Devuelve una tupla con las cantidades totales
    return (hombres, mujeres)

#3
def calculo_nombres(ruta: str, genero: str) -> set:
    # Lee los datos del fichero usando la función lee_nombres
    lista: List[FrecuenciaNombre] = lee_nombres(ruta)
    
    # Crea un conjunto para almacenar nombres únicos del género indicado
    Nombres = set()
    
    # Recorre los registros y añade los nombres que coinciden con el género
    for g in lista:
        if g.genero == genero:
            Nombres.add(g.nombre)
    
    # Devuelve el conjunto con los nombres encontrados
    return Nombres

#4
def calcular_top_nombres_de_año(ruta: str, año: int, genero: str, n: int) -> List[FrecuenciaNombre]:
    # Lee el fichero CSV y devuelve una lista de tuplas FrecuenciaNombre
    lista: List[FrecuenciaNombre] = lee_nombres(ruta)

    # Lista auxiliar para guardar los registros filtrados
    Nombres: List[FrecuenciaNombre] = []  

    # Filtra los registros que coinciden con el género y el año dados
    for g in lista:
        if g.genero == genero and g.año == año:
            Nombres.append(g)

    # Ordena la lista por el segundo campo (frecuencia), de mayor a menor
    Nombres.sort(key=lambda tupla: tupla[1], reverse=True)

    # Devuelve los n primeros registros (los más frecuentes)
    return Nombres[:n]

#5
def calcular_nombres_ambos_generos(ruta: str, año: int) -> set:
    # Lee los datos del fichero CSV y obtiene la lista completa de registros
    lista: List[FrecuenciaNombre] = lee_nombres(ruta)
    
    # Crea un conjunto con los nombres de hombres del año indicado
    nombres_hombre: set = set()
    for n in lista:
        if n.año == año and n.genero.lower() == "hombre":
            nombres_hombre.add(n.nombre)
    
    # Crea un conjunto con los nombres de mujeres del mismo año
    nombres_mujer: set = set()
    for n in lista:
        if n.año == año and n.genero.lower() == "mujer":
            nombres_mujer.add(n.nombre)
    
    # Devuelve los nombres que aparecen en ambos géneros (intersección)
    return nombres_hombre.intersection(nombres_mujer)

                                                     