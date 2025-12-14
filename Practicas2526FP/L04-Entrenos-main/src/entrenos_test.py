#entrenos_test.py
from entrenos import *

def test_lee_entrenos():
    entrenos = lee_entrenos('./data/entrenos.csv')
    print(f"Número de registros leídos: {len(entrenos)}")
    print(f"Los dos primeros: {entrenos[:2]}")
    print(f"Los dos últimos: {entrenos[-2:]}")

def test_filtra_por_tipo():
    entrenos = lee_entrenos('./data/entrenos.csv')
    tipo = 'Remo'
    resultado = filtra_por_tipo(entrenos, tipo)
    print(f"Los entrenamientos con el tipo {tipo} son: {resultado}")

def test_suma_de_calorias():
    entrenos = lee_entrenos('./data/entrenos.csv')

    tipo = 'Senderismo'
    resultado = suma_de_calorias(entrenos, tipo)
    print(f"Los entrenamientos con el tipo {tipo} han consumido: {resultado} calorias")

    tipo = 'Andar'
    resultado = suma_de_calorias(entrenos, tipo)
    print(f"Los entrenamientos con el tipo {tipo} han consumido: {resultado} calorias")

def test_obtiene_horas_más_perdida_peso_que():
    entrenos = lee_entrenos('./data/entrenos.csv')
    peso_min = 4.9
    resultado = obtiene_horas_más_perdida_peso_que(entrenos, peso_min)
    print(f"Las horas con más perdida de peso que {peso_min} kg. son: {resultado}")

def test_cuenta_distintos_tipos():
    entrenos = lee_entrenos('./data/entrenos.csv')
    resultado = cuenta_distintos_tipos(entrenos)
    print(f"El número de distinto tipos de entrenamiento es: {resultado}")

if __name__ == "__main__":
    test_lee_entrenos()
    test_filtra_por_tipo()
    test_suma_de_calorias()
    test_cuenta_distintos_tipos()
    test_obtiene_horas_más_perdida_peso_que()
    test_lee_entrenos()
    test_filtra_por_tipo()
    test_suma_de_calorias()
    test_cuenta_distintos_tipos()
    test_obtiene_horas_más_perdida_peso_que()


