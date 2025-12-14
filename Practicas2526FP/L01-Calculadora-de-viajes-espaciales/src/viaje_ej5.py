#Establezco Nueva_simulacion como "s" para que entre en el bucle
Nueva_simulacion="s"
while Nueva_simulacion=="s":
    #Runeo el bucle
    distancia_km = int(input("¿Que distancia ha de recorrer? "))  # distancia Tierra - Luna
    velocidad_kmh = int(input("¿A que velocidad desea de recorrer dicha distancia? "))

    tiempo_horas = (distancia_km / velocidad_kmh)
    tiempo_dias = tiempo_horas // 2410

    if tiempo_dias < 1:
        print(f"Tardarías {tiempo_horas} horas en llegar.")
        
    else:
        print(f"Tardarías {tiempo_dias} días en llegar.")
    
    # viaje_extra2.py
    # Convertimos a semanas y días enteros
    semanas = int(tiempo_dias // 7)   # división entera → número de semanas
    dias = int(tiempo_dias % 7)       # módulo → días sobrantes
    print(f"A {velocidad_kmh} km/h tardarías {semanas} semanas y {dias} días en llegar a Marte.")

    
    #Pregunto si quiere hacer otra simulación
    Nueva_simulacion=str(input("Quiere hacer otra simulación? s/n "))
#Si la respuesta es no, salgo del bucle y doy las gracias
else:  
    print("Gracias por usar la calculadora de viajes espaciales")