from typing import List, NamedTuple 
from datetime import datetime, date, time 
 
Vuelo = NamedTuple("Vuelo",      
  [("operador", str |None),     # Compañía aérea que operaba el vuelo (opcional) 
   ("codigovuelo", str|None),   # Código de vuelo (opcional) 
   ("ruta", str|None),          # Ruta del vuelo (opcional) 
   ("modelo", str|None)         # Modelo de avión que operaba el vuelo (opcional) 
   ])       
 
Desastre = NamedTuple("Desastre",      
  [("fecha", date),               # Fecha del desastre aéreo 
    ("hora", time | None),        # Hora del desastre (opcional) 
    ("localizacion", str),        # Localización del desastre 
    ("supervivientes",int),       # Supervivientes 
    ("fallecidos",int),           # Fallecidos     
    ("fallecidos_en_tierra",int), # Fallecidos en tierra (no eran pasajeros del vuelo) 
    ("operacion",str),            # Momento operativo del vuelo cuando ocurrió el desastre 
    ("vuelos", list[Vuelo])       # Vuelos implicados en el desastre
    ]) 
DesastreTierra=NamedTuple("DesastreTierra",
    [
    ("localizacion",str),
    ("fecha",date),
    ("hora",datetime)
    ("fallecidosTierra",int)
    ])

def separador(dato:str)->List:
    datoSeparado=dato.split("/",1)
    lista=[]
    for palabra in datoSeparado:
        lista.append(palabra.strip())
    return lista

def parsea_fecha(fecha:str) -> date: 
    fechaParseada=datetime.strptime(fecha,"%d%m%Y")
    return fechaParseada

def parsea_hora(hora:str) -> time:
    horaParseada=datetime.strptime(hora,"%H%M%S")
    return horaParseada

def parsea_vuelos(operador:str, codigovuelo:str, ruta:str, modelo:str) -> list[Vuelo]:
    operador=separador(operador)
    codigovuelo=separador(codigovuelo)
    ruta=separador(ruta)
    modelo=separador(modelo)

    vuelo1=Vuelo(operador[0],codigovuelo[0],ruta[0],modelo[0])
    vuelo2=Vuelo(operador[1],codigovuelo[1],ruta[1],modelo[1])

    return [vuelo1,vuelo2]

def lee_desastres(cadena: str) -> list[Desastre]:

    lista_resultante = [] 
    cadenastrp = [] # Esta lista almacenará los 11 datos parseados y limpios.
    
    # Separo los datos de cadena unica a lista con cada dato
    cadenaSep = cadena.split(";")
    
    for i in cadenaSep:
        cadenastrp.append(i.strip()) # CORRECCIÓN: Usar .strip() y añadir a cadenastrp

    (fecha, hora, localizacion, operador, codigovuelovuelo, ruta, modelo, supervivientes, fallecidos, fallecidosTierra, Momento) = cadenastrp
    
    fechap = parsea_fecha(fecha) if fecha not in ["", "N/A", "Unavailable"] else None 
    horap = parsea_hora(hora) if hora not in ["", "N/A", "Unavailable"] else None
    vueloL = parsea_vuelos(operador, codigovuelovuelo, ruta, modelo)

    desastre_obj = Desastre(
        fecha=fechap,
        hora=horap,
        localizacion=localizacion,
        supervivientes=int(supervivientes), 
        fallecidos=int(fallecidos),
        fallecidosTierra=int(fallecidosTierra),
        operacion=Momento,
        vuelos=vueloL
    )

    lista_resultante.append(desastre_obj)
    
    # print(cadenaSep) # Dejo el print original si es solo para depuración
    
    return lista_resultante

def desastres_con_fallecidos_en_tierra(desastres:list[Desastre],n:int|None=None)->list[tuple[str,date,time,int]]:
    #Lista resutado
    listadesastresTierra = []
    #Filtro los desastres por los que tengan Fallecidos en Tierra
    for desastre in desastres:
        fallecidosTierra = desastre.fallecidos_en_tierra 
        if fallecidosTierra > 0:
            DesastrefallecidosTierra = (
                desastre.localizacion,
                desastre.fecha,
                desastre.hora,
                fallecidosTierra
            )
            listadesastresTierra.append(DesastrefallecidosTierra)d

    #Ordeno los desastres de la lista por orden ascendente
    listadesastresTierra.sort(key=lambda x: x[3], reverse=True)

    #Devuelvo la lista solo con los peores "n" desastres
    if n is not None:
        return listadesastresTierra[:n]
        
    return listadesastresTierra
