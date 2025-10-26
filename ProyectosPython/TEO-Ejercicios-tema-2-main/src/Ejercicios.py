from typing import *
from datetime import *

def es_bisiesto(Año:int)->bool:
    Bisiesto=False
    if Año%400==0:
        Bisiesto=True
    elif Año%4==0 and Año%100!=0:
        Bisiesto=True
    return Bisiesto

def extrae_numeros(cadena:str)->list[int]:
    numeros=[]
    ristra=""
    for l in cadena:
        if l.isdigit():
            ristra=ristra + l
        else:
            if ristra!="":
                numeros.append(ristra)
                ristra=""
    if ristra!="":
        numeros.append(int(ristra))
    return numeros

from datetime import datetime, date
from typing import Tuple

def calcula_edad(cumple: datetime) -> Tuple[int, int]:
    hoy: date = date.today()
    dias: int = (hoy - cumple.date()).days
    edad: int = hoy.year - cumple.year

    # Si todavía no ha cumplido este año, resta uno a la edaD
    if (hoy.month, hoy.day) < (cumple.month, cumple.day):
        edad = edad - 1
        
    return (edad, dias)

def lee_variaciones_temperatura(ruta: str)-> List[Tuple[datetime, float]]:
    with open(ruta, )