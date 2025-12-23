import csv
from typing import List, NamedTuple, Optional # Agregamos Optional para compatibilidad
from datetime import datetime, date, time 
from collections import Counter # Necesario para el conteo de décadas

#####################################################################################################################################################################################################################################################

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
    ("hora",datetime), # Se mantiene 'datetime' aunque 'time' sería más preciso
    ("fallecidosTierra",int)
    ])

#####################################################################################################################################################################################################################################################
#DEFINO FUNCIONES PARA FACILITARME LA LECTURA DE LOS DESASTRES

def separador(dato:str)->List:
    datoSeparado=dato.split("/",1)
    lista=[]
    for palabra in datoSeparado:
        lista.append(palabra.strip())
    return lista

def parsea_fecha(fecha:str) -> date: 
    # CORRECCIÓN: Usar datetime.strptime y luego .date() para devolver el tipo correcto
    fechaParseada=datetime.strptime(fecha,"%d/%m/%Y") # Asumo el formato de tu CSV
    return fechaParseada.date()

def parsea_hora(hora:str) -> time:
    # CORRECCIÓN: Usar .time() para devolver el tipo 'time'
    horaParseada=datetime.strptime(hora,"%H:%M") # Asumo formato HH:MM
    return horaParseada.time()

def parsea_vuelos(operador:str, codigovuelo:str, ruta:str, modelo:str) -> list[Vuelo]:
    operador=separador(operador)
    codigovuelo=separador(codigovuelo)
    ruta=separador(ruta)
    modelo=separador(modelo)

    vuelo1=Vuelo(operador[0],codigovuelo[0],ruta[0],modelo[0])
    
    # Manejar si solo hay un vuelo, ya que tu parsea_vuelos espera 2 datos
    # Solo se crea el segundo vuelo si hay suficientes datos en la lista 'operador'
    if len(operador) > 1:
        vuelo2=Vuelo(operador[1],codigovuelo[1],ruta[1],modelo[1])
        return [vuelo1,vuelo2]
    else:
        return [vuelo1]


#####################################################################################################################################################################################################################################################
#CREO FUNCION PARA RECIBIR LA CADENA DE LOS DESASTRES Y PASARLO A UNA LISTA YA PARSEADA
def lee_desastres(cadena: str) -> list[Desastre]:

    lista_resultante = [] 
    cadenastrp = [] # Esta lista almacenará los 11 datos parseados y limpios.
    
    # Separo los datos de cadena unica a lista con cada dato    
    cadenaSep = cadena.split(";")
    
    for i in cadenaSep:
        cadenastrp.append(i.strip()) 

    (fecha, hora, localizacion, operador, codigovuelovuelo, ruta, modelo, supervivientes, fallecidos, fallecidosTierra, Momento) = cadenastrp
    
    # CORRECCIÓN: Fechas y Horas deben parsearse solo si hay datos válidos.
    # Si la fecha no es opcional en Desastre, parseamos directamente. Si fallara, se capturaría el error.
    fechap = parsea_fecha(fecha) 
    
    # Hora es opcional (time | None)
    horap = parsea_hora(hora) if hora not in ["", "N/A", "Unavailable"] else None
    
    vueloL = parsea_vuelos(operador, codigovuelovuelo, ruta, modelo)

    desastre_obj = Desastre(
        fecha=fechap,
        hora=horap,
        localizacion=localizacion,
        supervivientes=int(supervivientes), 
        fallecidos=int(fallecidos),
        fallecidos_en_tierra=int(fallecidosTierra), # Usar el nombre del campo de NamedTuple
        operacion=Momento,
        vuelos=vueloL
    )
    lista_resultante.append(desastre_obj)
    
    return lista_resultante
#####################################################################################################################################################################################################################################################
#LEE EL CSV, LO PASA A STR Y USA LEE_DESASTRES PARA PASARLO A LISTA Y ENTREGARLO
def lee_csv(ruta: str) -> List[Desastre]:
    listado_desastres: List[Desastre] = [] # Usando tu nomenclatura de tipo List[Desastre]
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector) # Saltamos la cabecera
        
        for fila_lista in lector:
            # Unir la lista de columnas en una única cadena separada por ";"
            cadena_unica = ";".join(fila_lista)
            
            # lee_desastres devuelve una lista con 1 Desastre
            desastres_de_linea = lee_desastres(cadena_unica)
            listado_desastres.extend(desastres_de_linea) # Agregamos el Desastre a la lista final
        
    return listado_desastres # Devolvemos la lista final
#####################################################################################################################################################################################################################################################

def desastres_con_fallecidos_en_tierra(desastres:list[Desastre],n:int|None=None)->list[tuple[str,date,time,int]]:
    #Lista resutado
    listadesastresTierra = []
    #Filtro los desastres por los que tengan Fallecidos en Tierra y Mapeo
    for desastre in desastres:
        fallecidosTierra = desastre.fallecidos_en_tierra 
        if fallecidosTierra > 0:
            DesastrefallecidosTierra = (
                desastre.localizacion,
                desastre.fecha,
                desastre.hora,
                fallecidosTierra
            )
            listadesastresTierra.append(DesastrefallecidosTierra)

    #Ordeno los desastres de la lista por orden descendente
    listadesastresTierra.sort(key=lambda x: x[3], reverse=True)

    #Devuelvo la lista solo con los peores "n" desastres
    if n is not None:
        return listadesastresTierra[:n]
        
    return listadesastresTierra
#####################################################################################################################################################################################################################################################

def decada_mas_colisiones(desastres:list[Desastre]) -> tuple[int,int]:
    
    # Usamos un diccionario para almacenar los conteos, respetando la lógica.
    conteo_por_decada = {}
    
    # 1. FILTRADO POR COLISIÓN (2 o más vuelos)
    for desastre in desastres:
        # Condición: El desastre debe tener 2 o más vuelos implicados.
        if len(desastre.vuelos) >= 2:
            
            # 2. CÁLCULO DE LA DÉCADA
            año = desastre.fecha.year
            # Fórmula para obtener las decadas
            decada = (año // 10) * 10
            
            # 3. AGRUPAMIENTO Y CONTEO (Lógica manual del diccionario)
            # Usamos 'in' para verificar si la década ya fue registrada
            if decada in conteo_por_decada:
                conteo_por_decada[decada] += 1
            else:
                conteo_por_decada[decada] = 1

    # 4. BÚSQUEDA DEL MÁXIMO
    
    # Si el diccionario está vacío (no hubo colisiones), devolvemos (0, 0)
    if not conteo_por_decada:
        return (0, 0)

    # Buscamos el par (década, conteo) con el mayor conteo usando max()
    # key=lambda item: item[1] le dice a max() que compare por el valor (el conteo)
    decada_maxima, max_colisiones = max(conteo_por_decada.items(), key=lambda item: item[1])
    
    # 5. RETORNO
    return (decada_maxima, max_colisiones)
########################################################################################################################################################################

