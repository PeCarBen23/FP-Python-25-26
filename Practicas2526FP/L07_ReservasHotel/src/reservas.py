import csv
from datetime import date, datetime
from typing import NamedTuple,List

#################################################################################################################################

# EJERCICIO 1
FechasEstancia = NamedTuple("FechasEstancia", [
    ("fecha_entrada", date),
    ("fecha_salida", date)
])

Reserva = NamedTuple("Reserva", [
    ("nombre", str),
    ("dni", str),
    ("fechas", FechasEstancia),
    ("tipo_habitacion", str),
    ("num_personas", int),
    ("precio_noche", float),
    ("servicios_adicionales", list[str]|None)
])

#################################################################################################################################

# EJERCICIO 2

def procesa_fecchas(fecha_entrada_txt: str, fecha_salida_txt: str) -> FechasEstancia:
    fecha_entrada: date = datetime.strptime(fecha_entrada_txt, "%d/%m/%Y").date()
    fecha_salida: date = datetime.strptime(fecha_salida_txt, "%d/%m/%Y").date()

    return FechasEstancia(fecha_entrada, fecha_salida)

def lee_reservas(ruta: str) -> List[Reserva]:
    res: List[Reserva] = []

    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)  # saltar cabecera
        for nombre, dni, fecha_entrada_txt, fecha_salida_txt, tipo_habitacion_txt, num_personas_txt, precio_txt, servicios_txt in lector:
            fechas: FechasEstancia = procesa_fecchas(fecha_entrada_txt,fecha_salida_txt)
            tipo_habitacion: str = str(tipo_habitacion_txt)
            num_personas: int = int(num_personas_txt)
            precio_noche: float = float(precio_txt.replace(",", "."))
            # Procesa servicios_adicionales:
            # - vacío o "None" -> lista vacía
            # - si hay texto -> lista de servicios separados por coma
            if servicios_txt.strip() == "" or servicios_txt.strip().lower() == "none":
                servicios_adicionales: list[str] = []
            else:
                servicios_adicionales = servicios_txt.split(",")


            reserva: Reserva = Reserva(
                nombre,
                dni,
                fechas,
                tipo_habitacion,
                num_personas,
                precio_noche,
                servicios_adicionales
            )
            res.append(reserva)
    return res
#################################################################################################################################

# EJERCICIO 3

def total_facturado(lista: List[Reserva],fecha_inicial: date | None,fecha_final: date | None) -> float:
     res=0
     for i in lista:    
         