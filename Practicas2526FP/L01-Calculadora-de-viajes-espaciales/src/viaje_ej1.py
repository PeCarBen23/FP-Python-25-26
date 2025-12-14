distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")

#viaje_extra2.py
# Convertimos a semanas y días enteros
#semanas = int(tiempo_dias // 7)   # división entera → número de semanas
#dias = int(tiempo_dias % 7)       # módulo → días sobrantes
    
#print(f"A {velocidad_kmh} km/h tardarías {semanas} semanas y {dias} días en llegar a Marte.")