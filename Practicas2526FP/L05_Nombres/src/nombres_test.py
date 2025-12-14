# nombres_test.py
from nombres import *


#Test 1
def test_frecuencias_nombres():
    print("1. test_frecuencias_nombres")
    ruta = ("/home/pedcarben/Documentos/Fedora Docs/Facultad/Asignaturas 3er año/FP 25-26/Practicas2526FP/Practicas2526FP/L05_Nombres/data/frecuencias_nombres.csv")   # ajusta la ruta si tu CSV está en otra carpeta
    lista = lee_nombres(ruta)

    print(f"\nLeídos {len(lista)} registros")

    print("Mostrando los 3 primeros:")
    print("   ", lista[:3])

    print("\nMostrando los 3 últimos:")
    print("   ", lista[-3:])

#Test 2
def test_filtrar_por_genero():
    # Ajusta esta ruta si tu CSV está en otra carpeta
    ruta: str = ("/home/pedcarben/Documentos/Fedora Docs/Facultad/Asignaturas 3er año/FP 25-26/Practicas2526FP/Practicas2526FP/L05_Nombres/data/frecuencias_nombres.csv")

    hombres, mujeres = frecuencias_generos(ruta)

    print("2. test_filtrar_por_genero")
    print(f"Número de registros para hombre: {hombres}")
    print()
    print("2. test_filtrar_por_genero")
    print(f"Número de registros para Mujer: {mujeres}")

#Test 3
def test_calcular_top_nombres_de_año():
    # Ajusta esta ruta si tu CSV está en otra carpeta
    ruta: str = ("/home/pedcarben/Documentos/Fedora Docs/Facultad/Asignaturas 3er año/FP 25-26/Practicas2526FP/Practicas2526FP/L05_Nombres/data/frecuencias_nombres.csv")

    top_nombres=calcular_top_nombres_de_año(ruta,2009,"Mujer",4)

    print("3. test_alcular_top_nombres_de_año")
    print(f"Top 5 nombres de mujer en 2009: {top_nombres}")

if __name__ == "__main__":
    # Ejecutar las pruebas
    test_frecuencias_nombres()
    test_filtrar_por_genero()
    test_calcular_top_nombres_de_año()

