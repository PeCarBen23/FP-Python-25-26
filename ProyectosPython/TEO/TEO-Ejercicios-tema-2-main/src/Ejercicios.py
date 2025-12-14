from typing import *
from datetime import *
from time import *
import csv

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
    #Creo la lista de tuplas
    ListaTuplas:List[Tuple[datetime,float]]=[]

    #Abro el csv y lo leo
    with open(ruta,encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)

    #Para cada registro=fecha,media en el csv lo almaceno como tupla en la lista
    for registro in lector:

        #Creo la tupla a guardar
        Año,Media=registro
        fecha=datetime.strptime(Año,"%m-%Y")
        media=float(Media)

        #Guardo la tupla en ListaTuplas
        ListaTuplas.append((fecha,media))
        print(f"{Año}: media {Media}")
        
    return ListaTuplas

    # def muestra_variaciones_temperatura(ruta:str)->None:
        
        