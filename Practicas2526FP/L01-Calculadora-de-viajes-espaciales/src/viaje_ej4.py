Distancia_marte_tierra_km = 225000000
for velocidad_kmh in [10000, 50001, 100000]:
    tiempo_horas = Distancia_marte_tierra_km / velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"A {velocidad_kmh} km/h tardarías {tiempo_dias} días en llegar a Marte.")
    
# viaje_extra2.py
# Convertimos a semanas y días enteros
# semanas = int(tiempo_dias // 7)   # división entera → número de semanas
# dias = int(tiempo_dias % 7)       # módulo → días sobrantes
    
# print(f"A {velocidad_kmh} km/h tardarías {semanas} semanas y {dias} días en llegar a Marte.")

