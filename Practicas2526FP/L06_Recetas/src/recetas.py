import csv
from datetime import *
from typing import *
from datetime import *

#####################################################################################################
#1
#tomate-3-u,cebolla-1-u,dietes ajo-4-u,caldo de verduras-500-cl,albahaca-10-gr
Ingrediente = NamedTuple("Ingrediente",
					     [("nombre",str),
						  ("cantidad",float),
						  ("unidad",str)])
				
#Sopa de Tomate;Entrante;Baja;tomate-3-u,cebolla-1-u,dietes ajo-4-u,caldo de verduras-500-cl,albahaca-10-gr;35;120;29/01/2024;8,5
Receta = NamedTuple("Receta", 
                    [("denominación", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", Optional[list[Ingrediente]]), #Es una opcion
                     #("ingerdientes,list[Ingrediente]/None"),
                     ("tiempo", int),
                     ("calorías", int),
                     ("fecha", date),
                     ("precio", float)])

#####################################################################################################
#2
#Mi Intento
# def lee_ingredientes(ruta:str)->list[Ingrediente] | None:
#     if not ruta:    #Si la ruta esta vacia 
#         return None #devuelvo None
    
#     res:List[Ingrediente]=[]
#     with open(ruta,encoding="utf-8") as f:
#         lector=csv.reader(f, delimiter="-")
#         next(lector)
        
#         for i in lector:
#             cantidad=i
#             cantidad=float(cantidad)
            
#             res.append(Ingrediente(i))
#     return res
            
#Del Profesor
def procesa_ingredientes(txt:str) -> list[Ingrediente] | None:
    if not txt:
        return None
    else:
        #fresas-5-u,piña-0.25-u,kiwi-1-u,menta-50-cl,zumo naranja-100-cl
        res:list[Ingrediente] = []
        ingredientes = txt.split(',')
        for ingr in ingredientes:
            #menta-50-cl                   #split("")->Cojo los datos deparados por (" ")
            nombre, cantidad, unidad = ingr.split('-')
            res.append(
                        Ingrediente(nombre, float(cantidad), unidad)
                      )


        return res

#Mi Intento
def lee_recetas(ruta:str)->list[Receta]:
    res:List[Receta]=[]
    with open(ruta,encoding="utf-8") as f:
        lector=csv.reader(f, delimiter=";")
        next(lector)

        for i in lector:
            
            i=Receta(ingredientes,tiempo,calorias,fecha,precio)
            ingredientes=procesa_ingredientes(ingredientes)
            tiempo=int(tiempo)  
            calorias=int(calorias)
            fecha=date.strftime(fecha,"%d/%m/%Y")
            precio=float(precio).replace("," , ".")

            res.append(i)
    return res

#####################################################################################################
#3

def diferentes_ingredientes(lista: List[Receta], unidad: Optional[str]) -> int:
    # Creamos un conjunto para guardar cada ingrediente sin repetir
    ingredientes_distintos: set[str] = set()

    # Recorremos todas las recetas de la lista
    for receta in lista:
        if receta.ingredientes:
            # Recorremos los ingredientes dentro de cada receta
            for ingrediente in receta.ingredientes:
                # Si no se filtra por unidad (unidad == None), los añadimos todos
                # Si sí se filtra, añadimos solo los que coinciden en unidad
                if unidad is None or ingrediente.unidad == unidad:
                    ingredientes_distintos.add(ingrediente.nombre)

    return len(ingredientes_distintos)

#####################################################################################################
#4
def recetas_con_ingredientes(lista: List[Receta], ingredientes: set[str]) -> List[Tuple[str, float, float]]:
    res:list[tuple[str,float,float]]

    for receta in lista:
        if ingredientes:
            for ingrediente in ingredientes:
                if ingrediente in receta:
                    tupla=(receta.denominación,receta.calorías,receta.precio)
                    res.append(tupla)
    res.sort(key=lambda tupla:tupla[2],reverse=True)
    return tupla

#####################################################################################################
#5        CHAT GPT
def receta_mas_barata(recetas: list[Receta], tipos: set[str], n: int | None = None) -> Receta | None:
    # Filtra por tipos indicados
    candidatas: list[Receta] = []
    for r in recetas:
        if r.tipo in tipos:
            candidatas.append(r)

    # Si no hay candidatas, no hay resultado
    if len(candidatas) == 0:
        return None

    # Si n es None, buscamos la receta más barata entre todas las candidatas
    if n is None:
        mas_barata: Receta = candidatas[0]
        for r in candidatas:
            if r.precio < mas_barata.precio:
                mas_barata = r
        return mas_barata

    # Ordena candidatas por calorías ascendente
    ordenadas_por_cal: list[Receta] = candidatas[:]
    ordenadas_por_cal.sort(key=lambda r: r.calorías)

    # Toma las n primeras (si n > len, toma todas)
    top_n: list[Receta] = []
    contador: int = 0
    tope: int = int(n)
    for r in ordenadas_por_cal:
        if contador < tope:
            top_n.append(r)
            contador = contador + 1
        else:
            break

    # Si top_n queda vacío (por ejemplo n=0), no hay resultado
    if len(top_n) == 0:
        return None

    # Entre esas n, busca la más barata (menor precio)
    mas_barata: Receta = top_n[0]
    for r in top_n:
        if r.precio < mas_barata.precio:
            mas_barata = r

    # Devuelve la receta encontrada
    return mas_barata
