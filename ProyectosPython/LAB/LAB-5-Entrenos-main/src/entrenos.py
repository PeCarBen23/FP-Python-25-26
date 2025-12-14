from collections import *
from typing import *
from datetime import datetime
import csv

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
def lee_entrenos(ruta:str)->List[Entreno]:
    res:List[Entreno]=[]
    with open(ruta,encoding="utf-8") as f:
      lector=csv.reader
      next(lector)
      for i in lector:
        #Almaceno los datos en i
            tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido=i
        #Parseo los datos
        #Los tipo str, puedes o name=name o simplemente no ponerlo,
        #pero si no lo pones hay que quitarlo del i
            tipo=tipo
            fechahora=datetime.strptime(fechahora,"%d/%m/%Y %H:%M")
            ubicacion=ubicacion
            duracion=int(duracion)
            calorias=int(calorias)
            distancia=float(distancia)
            frecuencia=int(frecuencia)
        #de tipo bool (S si ha sido compartido, N si no lo ha sido).
            if compartido=="S":
               compartido=True
            else:   
               compartido=False
            res.append(Entreno[i])
    return res