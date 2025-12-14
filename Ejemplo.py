####################################################################################################
# 0. Leer y Parsear un CSV
####################################################################################################
def funcion(ruta: str) -> Salida:
    # Crear la estructura de salida (normalmente una lista)
    res: Salida = []      # SOLO si la salida es una lista

    # Abrir el fichero CSV
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)  # Saltar cabecera

        # Leer cada registro del CSV
        for campo1_txt, campo2_txt, campo3_txt, ... in lector:

            # 1) Convertir tipos (parsing)
            campo1 = tipo1(campo1_txt)
            campo2 = tipo2(campo2_txt)
            campo3 = tipo3(campo3_txt)
            ...

            # 2) Crear la tupla NamedTuple o estructura correspondiente
            registro: NombreTupla = NombreTupla(
                campo1,
                campo2,
                campo3,
                ...
            )

            # 3) Añadir a la lista resultado
            res.append(registro)

    # Devolver la estructura resultante
    return res

from typing import *
from datetime import date, datetime, time
import csv


####################################################################################################
# 1. PLANTILLA: DEFINICIÓN DE NamedTuple SENCILLA (SIN FECHAS)
####################################################################################################

# Ejemplo típico: datos de compras, entrenos, extranjería, etc.
# Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra)
# RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres)

Compra = NamedTuple("Compra", [
    ("dni", str),
    ("supermercado", str),
    ("provincia", str),
    ("fecha_llegada", datetime),
    ("fecha_salida", datetime),
    ("total_compra", float)
])

# Uso:
# compra = Compra("62745110Y", "Carrefour", "Sevilla", datetime(...), datetime(...), 175.71)


####################################################################################################
# 2. PLANTILLA: NamedTuple CON FECHAS (date) Y HORAS (time)
####################################################################################################

# Muy típico en reservas de hotel, festivales, F1, etc.
# FechasEstancia(fecha_entrada, fecha_salida)
FechasEstancia = NamedTuple("FechasEstancia", [
    ("fecha_entrada", date),
    ("fecha_salida", date)
])

# Reserva(nombre, dni, fechas, tipo_habitacion, num_personas, precio_noche, servicios_adicionales)
Reserva = NamedTuple("Reserva", [
    ("nombre", str),
    ("dni", str),
    ("fechas", FechasEstancia),
    ("tipo_habitacion", str),
    ("num_personas", int),
    ("precio_noche", float),
    ("servicios_adicionales", list[str] | None)
])

# Artista(nombre, hora_comienzo, cache)
Artista = NamedTuple("Artista", [
    ("nombre", str),
    ("hora_comienzo", time),
    ("cache", int)
])

# Festival(nombre, fecha_comienzo, fecha_fin, estado, precio, entradas_vendidas, artistas, top)
Festival = NamedTuple("Festival", [
    ("nombre", str),
    ("fecha_comienzo", date),
    ("fecha_fin", date),
    ("estado", str),
    ("precio", float),
    ("entradas_vendidas", int),
    ("artistas", List[Artista]),
    ("top", bool)
])


####################################################################################################
# 3. PLANTILLA: PARSEAR FECHAS Y HORAS DESDE CSV
####################################################################################################

# Comentario general:
# - Para fechas tipo "2024-07-19": formato "%Y-%m-%d"
# - Para fechas tipo "21/11/2022": formato "%d/%m/%Y"
# - Para datetime tipo "01/01/2019 14:43": formato "%d/%m/%Y %H:%M"
# - Para horas tipo "20:30": formato "%H:%M"

def parsea_fecha_iso(txt: str) -> date:
    # Convierte "2024-07-19" en date(2024, 7, 19)
    return datetime.strptime(txt, "%Y-%m-%d").date()


def parsea_fecha_barra(txt: str) -> date:
    # Convierte "21/11/2022" en date(2022, 11, 21)
    return datetime.strptime(txt, "%d/%m/%Y").date()


def parsea_datetime(txt: str) -> datetime:
    # Convierte "01/01/2019 14:43" en datetime(2019, 1, 1, 14, 43)
    return datetime.strptime(txt, "%d/%m/%Y %H:%M")


def parsea_hora(txt: str) -> time:
    # Convierte "20:30" en time(20, 30)
    return datetime.strptime(txt, "%H:%M").time()


####################################################################################################
# 4. PLANTILLA GENERAL: LECTURA DE CSV A LISTA DE NamedTuple
####################################################################################################

# Esta es la plantilla que tú mismo ya estabas usando, afinada.
# Vale para TODO: reservas, festivales, f1, compras, extranjería…

def lee_compras(ruta: str) -> List[Compra]:
    # Lista resultado
    res: List[Compra] = []

    # Abrir el fichero
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")   # o ";" según el fichero
        next(lector)                            # saltar cabecera

        # Recorrer registros
        for dni_txt, super_txt, prov_txt, flleg_txt, fsal_txt, total_txt in lector:
            # Parseo de tipos
            dni = str(dni_txt)
            supermercado = str(super_txt)
            provincia = str(prov_txt)
            fecha_llegada = parsea_datetime(flleg_txt)
            fecha_salida = parsea_datetime(fsal_txt)
            total_compra = float(total_txt.replace(",", "."))

            # Crear la tupla
            compra: Compra = Compra(
                dni,
                supermercado,
                provincia,
                fecha_llegada,
                fecha_salida,
                total_compra
            )

            # Añadir a la lista
            res.append(compra)

    return res


####################################################################################################
# 5. PLANTILLA: PROCESAR UN CAMPO “COMPLEJO” DEL CSV (LISTAS, INGREDIENTES, VUELTAS, SERVICIOS…)
####################################################################################################

# a) Ejemplo típico: procesar ingredientes "tomate-3-u,cebolla-1-u,caldo-0.5-l"

Ingrediente = NamedTuple("Ingrediente", [
    ("nombre", str),
    ("cantidad", float),
    ("unidad", str)
])

def procesa_ingredientes(txt: str) -> List[Ingrediente] | None:
    # Si la cadena está vacía, devolvemos None
    if not txt:
        return None

    # Lista resultado
    res: List[Ingrediente] = []

    # Separamos por comas cada ingrediente
    partes = txt.split(",")

    for parte in partes:
        # Ejemplo: "tomate-3-u"
        nombre_txt, cantidad_txt, unidad_txt = parte.split("-")

        nombre = str(nombre_txt)
        cantidad = float(cantidad_txt.replace(",", "."))
        unidad = str(unidad_txt)

        ing: Ingrediente = Ingrediente(nombre, cantidad, unidad)
        res.append(ing)

    return res


# b) Ejemplo F1: lista con tiempos tipo "[31.254/ 31.567/ 31.789/ 32.045/ -/ -]"
# Donde "-" significa 0 (int) y el resto son float

def procesa_vueltas(txt: str) -> List[int | float]:
    # Quitamos corchetes y espacios
    txt = txt.strip()
    txt = txt.removeprefix("[")
    txt = txt.removesuffix("]")

    # Separar por "/"
    partes = txt.split("/")

    res: List[int | float] = []

    for p in partes:
        valor_txt = p.strip()
        if valor_txt == "-" or valor_txt == "":
            res.append(0)
        else:
            res.append(float(valor_txt))

    return res


# c) Ejemplo servicios_adicionales: "Parking-Gimnasio-Spa" o "" (vacío)

def procesa_servicios(txt: str) -> List[str] | None:
    # Si está vacío => None (o [] según el enunciado)
    if not txt:
        return []

    servicios: List[str] = []

    partes = txt.split("-")
    for s in partes:
        servicio = s.strip()
        if servicio != "":
            servicios.append(servicio)

    # Según el enunciado de reservas, a veces piden lista vacía, no None
    return servicios


####################################################################################################
# 6. PLANTILLA: LECTURA CON FECHAS AGRUPADAS EN OTRA NamedTuple (RESERVAS HOTEL) :contentReference[oaicite:1]{index=1}
####################################################################################################

def lee_reservas(ruta: str) -> List[Reserva]:
    res: List[Reserva] = []

    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)

        for nombre_txt, dni_txt, f_entrada_txt, f_salida_txt, tipo_txt, num_txt, precio_txt, servicios_txt in lector:
            # Parseo básico
            nombre = str(nombre_txt)
            dni = str(dni_txt)

            # Fechas de entrada y salida
            fecha_entrada = parsea_fecha_barra(f_entrada_txt)
            fecha_salida = parsea_fecha_barra(f_salida_txt)
            fechas = FechasEstancia(fecha_entrada, fecha_salida)

            tipo_habitacion = str(tipo_txt)
            num_personas = int(num_txt)

            # Precio con coma o punto
            precio_noche = float(precio_txt.replace(",", "."))

            # Servicios adicionales
            lista_servicios = procesa_servicios(servicios_txt)

            reserva: Reserva = Reserva(
                nombre,
                dni,
                fechas,
                tipo_habitacion,
                num_personas,
                precio_noche,
                lista_servicios
            )

            res.append(reserva)

    return res


####################################################################################################
# 7. PLANTILLA: FUNCIONES CON FECHAS Y RANGOS (total_facturado, filtros, etc.) 
####################################################################################################

def total_facturado_reservas(reservas: List[Reserva],
                             fecha_ini: Optional[date] = None,
                             fecha_fin: Optional[date] = None) -> float:
    # Devuelve el total facturado entre fecha_ini y fecha_fin (ambas incluidas).
    total: float = 0.0

    for r in reservas:
        fecha_ent = r.fechas.fecha_entrada

        # Comprobar límite inferior
        if fecha_ini is not None and fecha_ent < fecha_ini:
            continue

        # Comprobar límite superior
        if fecha_fin is not None and fecha_ent > fecha_fin:
            continue

        # Número de días de la reserva
        dias = (r.fechas.fecha_salida - r.fechas.fecha_entrada).days

        importe = dias * r.precio_noche
        total = total + importe

    return total


####################################################################################################
# 8. PLANTILLA: FILTRAR, CONTAR, SUMAR, TOP-N, DICCIONARIOS (PATRONES GENÉRICOS)
####################################################################################################

# a) Filtrar por condición (ej: reservas de un tipo)

def filtra_por_tipo_habitacion(reservas: List[Reserva], tipo: str) -> List[Reserva]:
    res: List[Reserva] = []
    for r in reservas:
        if r.tipo_habitacion == tipo:
            res.append(r)
    return res


# b) Contar elementos (ej: cuántas reservas con un servicio)

def cuenta_reservas_con_servicio(reservas: List[Reserva], servicio: str) -> int:
    contador: int = 0
    for r in reservas:
        if r.servicios_adicionales is not None:
            if servicio in r.servicios_adicionales:
                contador = contador + 1
    return contador


# c) Top-N genérico (ordenar por algo y coger los n primeros)

def top_n_por_precio(reservas: List[Reserva], n: int) -> List[Reserva]:
    # Copia de la lista para no modificar la original
    copia: List[Reserva] = list(reservas)

    # Ordenamos por precio_noche descendente
    copia.sort(key=lambda r: r.precio_noche, reverse=True)

    # Devolvemos los n primeros
    return copia[:n]


# d) Diccionario de acumulación (ej: total por DNI, por tipo, por mes, etc.)

def total_por_dni(reservas: List[Reserva]) -> Dict[str, float]:
    totales: Dict[str, float] = {}

    for r in reservas:
        dni = r.dni

        # Calcular importe de esta reserva
        dias = (r.fechas.fecha_salida - r.fechas.fecha_entrada).days
        importe = dias * r.precio_noche

        if dni not in totales:
            totales[dni] = 0.0

        totales[dni] = totales[dni] + importe

    return totales


####################################################################################################
# 9. PLANTILLA: FUNCIÓN QUE DEVUELVE SET/LIST DE VALORES DISTINTOS
####################################################################################################

def tipos_habitacion_distintos(reservas: List[Reserva]) -> List[str]:
    # Usamos set para evitar repetidos
    tipos_set: Set[str] = set()

    for r in reservas:
        tipos_set.add(r.tipo_habitacion)

    # Lo convertimos a lista y lo ordenamos
    tipos_lista: List[str] = list(tipos_set)
    tipos_lista.sort()
    return tipos_lista


####################################################################################################
# 10. PLANTILLA: TESTS AL ESTILO “PEDRO"
####################################################################################################

# Ejemplo de test que encaja con tu estilo:
# - import *
# - función test_
# - prints en español
# - ejecución desde main

def test_lee_reservas():
    print("test_lee_reservas")
    ruta: str = "./data/reservas.csv"   # ajustar ruta

    lista: List[Reserva] = lee_reservas(ruta)

    print(f"Total reservas: {len(lista)}")
    print("Las tres primeras:")
    print("   ", lista[:3])


def test_total_facturado_reservas():
    print("test_total_facturado_reservas")

    ruta: str = "./data/reservas.csv"
    lista: List[Reserva] = lee_reservas(ruta)

    total = total_facturado_reservas(lista, None, None)
    print(f"Total facturado entre None y None: {total}")


if __name__ == "__main__":
    # Ejemplos de uso de las plantillas
    # (comenta o descomenta según lo que quieras probar)
    # test_lee_reservas()
    # test_total_facturado_reservas()
    pass

