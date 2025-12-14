edad_usuario = int(input("¿Cuál es tu edad? "))
Nivel_fisico_usuario = 0

# Pedir nivel físico con validación mediante while
while Nivel_fisico_usuario <= 1 or Nivel_fisico_usuario > 10:
    Nivel_fisico_usuario = int(input("¿Cuál es tu nivel físico de 1 a 10? "))
# Si el nivel físico no esta dentro del rango, mostrar mensaje de error y pedir de nuevo
    if Nivel_fisico_usuario <0 or Nivel_fisico_usuario > 10:
        print(" El nivel físico debe estar entre 1 y 10.")

# Lógica principal
if edad_usuario < 18:
    print("Eres demasiado joven para viajar al espacio")
elif Nivel_fisico_usuario < 5:
    print("Tu nivel físico es demasiado bajo para viajar al espacio")
else:
    print("Eres apto para viajar al espacio")
    
