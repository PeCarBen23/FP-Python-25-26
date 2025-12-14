distancia_km = int(input("¿Que distancia ha de recorrer? "))  # distancia Tierra - Luna
velocidad_kmh = int(input("¿A que velocidad desea de recorrer dicha distancia? "))
tiempo_horas = (distancia_km / velocidad_kmh)
tiempo_dias = tiempo_horas // 24
if tiempo_dias < 1:
    print(f"Tardarías {tiempo_horas} horas en llegar.")
else:
    print(f"Tardarías {tiempo_dias} días en llegar.")
    
#viaje_extra2.py
# Convertimos a semanas y días enteros
# semanas = int(tiempo_dias // 7)   # división entera → número de semanas
# dias = int(tiempo_dias % 7)       # módulo → días sobrantes
    
# print(f"A {velocidad_kmh} km/h tardarías {semanas} semanas y {dias} días en llegar a Marte.")

