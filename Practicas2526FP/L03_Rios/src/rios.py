from typing import NamedTuple

Rio=NamedTuple("Rio", [("nombre",str),("longitud",int),("continente",str)])

rios = [Rio("Amazonas", 7062, "América del Sur"), Rio("Nilo", 6853, "África"),
        Rio("Yangtsé", 6300, "Asia"), Rio("Misisipi", 6275, "América del Norte"),
        Rio("Amarillo", 5464, "Asia"), Rio("Mekong", 4880, "Asia"),
        Rio("Congo", 4700, "África"), Rio("Danubio", 2850, "Europa")]


# #1
# def carga_rios(rios):
#     lista_rios=[]
#     for r in rios:
#         lista_rios.append(r)
#     # print(lista_rios)
#     return lista_rios

# #2
def filtra_rios_de_continente(rios: list, continente: str) -> list:
    lista_rios_continente = []
    for r in rios:
        if r.continente == continente:
            lista_rios_continente.append(r.nombre)
    # print(lista_rios_continente)
    return lista_rios_continente

# #3
# def obtener_continentes_y_rios(rios:list,continente:str)->list:
#     lista_continentes_y_rios=[]
#     RioContinente=NamedTuple("RioContinente",[("rio",str),("continente",str)])
#     for r in rios:
#         if r.continente == continente:
#             lista_continentes_y_rios.append(RioContinente(r.nombre,r.continente))
#     return lista_continentes_y_rios
    
#4
# def contar_diferentes_continentes(rios:list[Rio])->int:
#     lista_continentes_rios_largos={c.continente for c in rios if c.longitud>6300}
#     Lista_continentes_ordenados=sorted(lista_continentes_rios_largos)
#     # print(Lista_continentes_ordenados)
#     return len(Lista_continentes_ordenados)
# contar_diferentes_continentes(rios)

#5
# def suma_longitudes(rios: list[Rio], continentes: set[str]) -> int:
#     return sum(r.longitud for r in rios if r.continente in continentes)

#6
def rio_con_nombre_mas_corto(rios: list[Rio], continentes: set[str]) -> str:

    rios_filtrados = []
    for r in rios:
        if r.continente in continentes:
            rios_filtrados.append(r)

    rio_mas_corto = rios_filtrados[0]
    for r in rios_filtrados:
        if len(r.nombre) < len(rio_mas_corto.nombre):
            print(r)
            rio_mas_corto = r
    return rio_mas_corto.nombre



#7

#Foto Movil

    


