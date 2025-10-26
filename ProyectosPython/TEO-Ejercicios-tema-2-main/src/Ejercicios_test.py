from Ejercicios import *

def test_es_bisiesto():
    Año=int(input("Introduzca un año: "))
    print(es_bisiesto(Año))

def test_extrae_nuermos():
    cadena=" Este año la empresa ganó 12432 euros de 8 contratos 43"
    print(extrae_numeros(cadena))

def test_calcula_edad():
    cumple=datetime(2005,5,6)
    print(calcula_edad(cumple))


if __name__ == "__main__":
    #test_es_bisiesto()
    #test_extrae_nuermos()
    test_calcula_edad()