from typing import NamedTuple,List,Set,Tuple,Dict,Optional 
from datetime import datetime,date 
import csv
 
Commit = NamedTuple("Commit",      
       [("id", str), # Identificador alfanumérico del commit 
        ("mensaje", str), # Mensaje asociado al commit 
        ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit 
       ]) 
Repositorio = NamedTuple("Repositorio",      
      [("nombre", str),  # Nombre del repositorio 
       ("propietario", str), # Nombre del usuario propietario 
       ("lenguajes", Set[str]),  # Conjunto de lenguajes usados 
       ("privado", bool),  # Indica si es privado o público 
       ("commits", List[Commit])  # Lista de commits realizados 
       ])


def parsea_commits(commit:str)->List[Commit]:
    res=[]
    commitsLista=[]
    datos=[]
    #Separo cada commit independiente separados por ; en la cadena
    commitsLista.append(commit.split(";"))
    #Separo cada dato independiente separados por # en el commit
    datos.append(commitsLista.split("#"))
    id=datos[0]
    mensaje=datos[1]
    fecha_hora=datos[2].datetime()
    Commit=Commit(id,mensaje,fecha)
    res.append(Commit)











# def lee_repositorios(csv_filename: str) -> List[Repositorio]:
#     res: List[Repositorio] = []

#     with open(ruta,encoding="utf-8") as f:
#         lector=csv.reader(f,delimiter=",")
#         next(lector)

    

#     return res
