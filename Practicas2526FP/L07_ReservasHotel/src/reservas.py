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
def parseaFecha(fecha: str) -> date:
    fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
    return fecha

def parseaServicios(servicios_adicionales: str) -> list[str] | None:
    if not servicios_adicionales:
        return None
    else:
        listaServicios=servicios_adicionales.split(",")
    return listaServicios
    

def lee_reservas(fichero: str) -> List[Reserva]:
    res: List[Reserva] = []
    with open(fichero, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)

        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales in lector:
            # nombre, dni y tipo_habitacion no se parsean ya que son str
            fecha_entradap = parseaFecha(fecha_entrada)
            fecha_salidap = parseaFecha(fecha_salida)
            num_personasp = int(num_personas)
            precio_nochep = float(precio_noche)
            servicios_adicionalesp = parseaServicios(servicios_adicionales)
            
            fechasp = FechasEstancia(fecha_entradap, fecha_salidap)
            
            # Usamos la variable 'fechas' en el constructor de Reserva
            res.append(Reserva(nombre, dni, fechasp, tipo_habitacion, 
                               num_personasp, precio_nochep, servicios_adicionalesp))
        
        return res

#################################################################################################################################

# EJERCICIO 3

def total_facturado(lista: List[Reserva],fecha_inicial: date | None,fecha_final: date | None) -> float:
     res=0
     for i in lista:
         if (fecha_inicial == None or i.fechas.fecha_entrada >= fecha_inicial) and (fecha_final == None or i.fechas.fecha_entrada <= fecha_final):
             dias = (i.fechas.fecha_salida - i.fechas.fecha_entrada).days
             res += dias * i.precio_noche
     return res