from festivales import *


def test_lee_festivales():
    festivales = lee_festivales('data/festivales.csv')
    
    print(f"Número de registros: {len(festivales)}")
    
    print("\nTres primeros festivales:")
    for festival in festivales[:3]:
        print(festival)
    
    print("\nTres últimos festivales:")
    for festival in festivales[-3:]:
        print(festival)


def test_total_facturado():
    festivales = lee_festivales('data/festivales.csv')
    
    print("Test Ej2: total_facturado")
    
    total1 = total_facturado(festivales, None, None)
    print(f"    Entre None y None el total es: {total1}")
    
    total2 = total_facturado(festivales, None, date(2024, 6, 15))
    print(f"    Entre None y 2024-06-15 el total es: {total2}")
    
    total3 = total_facturado(festivales, date(2024, 6, 15), None)
    print(f"    Entre 2024-06-15 y None el total es: {total3}")
    
    total4 = total_facturado(festivales, date(2024, 6, 1), date(2024, 6, 15))
    print(f"    Entre 2024-06-01 y 2024-06-15 el total es: {total4}")
    
    total5 = total_facturado(festivales, date(2024, 6, 1), date(2024, 6, 23))
    print(f"    Entre 2024-06-01 y 2024-06-23 el total es: {total5}")


def test_artista_top():
    festivales = lee_festivales('data/festivales.csv')
    
    print("Test Ej3: artista_top")
    artista = artista_top(festivales)
    
    # Contar cuántos festivales tiene ese artista
    contador = 0
    for festival in festivales:
        for a in festival.artistas:
            if a.nombre == artista:
                contador += 1
                break
    
    print(f"    El artista que ha actuado en más festivales es {artista}, con {contador} festivales.")


def test_mes_beneficio_medio_mas_rentable():
    festivales = lee_festivales('data/festivales.csv')
    
    print("Test Ej4: mes_beneficio_medio_mas_rentable")
    mes = mes_mayor_beneficio_medio(festivales)
    print(f"    El mes con más beneficio es {mes}.")


def test_artistas_comunes():
    festivales = lee_festivales('data/festivales.csv')
    
    print("Test 5: artistas_comunes")
    
    comunes1 = artistas_comunes(festivales, "Creamfields", "Tomorrowland")
    print(f"    Los artistas comunes entre Creamfields y Tomorrowland son {comunes1}")
    
    comunes2 = artistas_comunes(festivales, "Primavera Sound", "Coachella")
    print(f"    Los artistas comunes entre Primavera Sound y Coachella son {comunes2}")
    
    comunes3 = artistas_comunes(festivales, "Iconica Fest", "Primavera Sound")
    print(f"    Los artistas comunes entre Iconica Fest y Primavera Sound son {comunes3}")


def test_festivales_top_mejor_ratio():
    festivales = lee_festivales('data/festivales.csv')
    
    print("Test 6: festivales_top_mejor_ratio")
    
    resultado1 = festivales_top_calidad_por_duracion(festivales, 1)
    print("    Los mejores 1 festivales por número de días son:")
    for dias, nombres in resultado1.items():
        print(f"    {dias}: {nombres}")
    
    resultado3 = festivales_top_calidad_por_duracion(festivales, 3)
    print("    Los mejores 3 festivales por número de días son:")
    for dias, nombres in resultado3.items():
        print(f"    {dias}: {nombres}")


if __name__ == "__main__":
    test_lee_festivales()
    print()
    test_total_facturado()
    print()
    test_artista_top()
    print()
    test_mes_beneficio_medio_mas_rentable()
    print()
    test_artistas_comunes()
    print()
    test_festivales_top_mejor_ratio()
