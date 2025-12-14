#entrenos.py
from typing import *
from datetime import datetime
import csv

# Definición de la tupla Entreno
Entreno = NamedTuple("Entreno", [
    ("tipo", str),
    ("fechahora", datetime),
    ("ubicacion", str),
    ("duracion", int),
    ("calorias", int),
    ("distancia", float),
    ("frecuencia", int),
    ("compartido", bool)
])

def lee_entrenos(ruta: str) -> List[Entreno]:
    # Lee el fichero CSV y devuelve una lista de tuplas Entreno
    res: List[Entreno] = []

    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        next(lector)

        for registro in lector:
            fechahora,duracion,calorias,distancia,frecuencia,compartido=registro
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            if compartido == "S":
                compartido = True
            else:
                compartido = False
            res.append(Entreno(registro))
    return res


def tipos_entreno(lista: List[Entreno]) -> List[str]:
    # Devuelve los tipos de entrenamiento únicos y ordenados alfabéticamente
    tipos: List[str] = []
    for e in lista:
        if e.tipo not in tipos:
            tipos.append(e.tipo)
    tipos.sort()
    return tipos


def entrenos_duracion_superior(lista: List[Entreno], d: int) -> List[Entreno]:
    # Devuelve los entrenos con duración mayor que d minutos
    res: List[Entreno] = []
    for e in lista:
        if e.duracion > d:
            res.append(e)
    return res


def suma_calorias(lista: List[Entreno], f_inicio: datetime, f_fin: datetime) -> int:
    # Devuelve la suma de calorías de los entrenos entre dos fechas (ambas incluidas)
    total = 0
    for e in lista:
        if e.fechahora >= f_inicio and e.fechahora <= f_fin:
            total = total + e.calorias
    return total


def entrenamiento_mas_kms(lista: List[Entreno]) -> Optional[Entreno]:
    # Devuelve el entrenamiento con más kilómetros recorridos
    if len(lista) == 0:
        return None

    mayor = lista[0]
    for e in lista:
        if e.distancia > mayor.distancia:
            mayor = e
    return mayor


def duracion_media_entrenos(lista: List[Entreno], anio: int, mes: int) -> Optional[float]:
    # Devuelve la duración media de los entrenamientos del mes y año indicados
    total = 0
    contador = 0
    for e in lista:
        if e.fechahora.year == anio and e.fechahora.month == mes:
            total = total + e.duracion
            contador = contador + 1

    if contador == 0:
        return None
    else:
        media = total / contador
        return float(media)

from typing import *
from datetime import datetime

# ... (tu código actual arriba sin cambios)

def filtra_por_tipo(lista: List[Entreno], tipo_entreno: str) -> List[Tuple[str, float]]:
    # Filtra entrenos por tipo y devuelve (ubicacion, distancia)
    res: List[Tuple[str, float]] = []
    for e in lista:
        if e.tipo == tipo_entreno:
            res.append((e.ubicacion, e.distancia))
    return res


def suma_de_calorias(lista: List[Entreno], tipo_entreno: str) -> int:
    # Suma las calorías de los entrenos del tipo indicado
    total = 0
    for e in lista:
        if e.tipo == tipo_entreno:
            total = total + e.calorias
    return total


def obtiene_horas_más_perdida_peso_que(lista: List[Entreno], peso_min: float) -> List[int]:
    # Devuelve horas (0..23) cuya pérdida de peso estimada supera peso_min kg
    # Conversión aproximada: 1 kg ≈ 7700 kcal
    KCAL_POR_KG = 7700.0

    kcal_por_hora: Dict[int, int] = {}
    for e in lista:
        hora = e.fechahora.hour
        if hora not in kcal_por_hora:
            kcal_por_hora[hora] = 0
        kcal_por_hora[hora] = kcal_por_hora[hora] + e.calorias

    horas: List[int] = []
    for hora in kcal_por_hora:
        kg = float(kcal_por_hora[hora]) / KCAL_POR_KG
        if kg > peso_min:
            horas.append(hora)

    horas.sort()
    return horas


def cuenta_distintos_tipos(lista: List[Entreno]) -> int:
    # Cuenta tipos de entreno distintos (tal cual aparecen)
    tipos: List[str] = []
    for e in lista:
        if e.tipo not in tipos:
            tipos.append(e.tipo)
    return len(tipos)

