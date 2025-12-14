import random
#A
def cargar_palabras(ruta:str)->list[str]:
    ''' 
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.    
    
    :param ruta: Ruta de un fichero de texto. El fichero debe contener una palabra por línea.
    :type ruta: str
    :return: Una lista con las palabras leías del fichero
    :rtype: list[str]
    '''
    palabras = ['python', 'programacion', 'computadora', 'juego', 'ahorcado', 'raton', 'seda', 'banda', 'bosque', 'pulso', 'yunque', 'huracan', 'vidrio', 'cruce', 'oso', 'aroma', 'lancha', 'duelo', 'pared', 'musica', 'regalo', 'angulo', 'belleza', 'eco', 'nube', 'camino', 'sentido', 'poder', 'cocina', 'jabon', 'paloma', 'carne', 'gafas', 'ruido', 'llanto', 'piel', 'fuerza', 'sombra', 'viento', 'familia', 'templo', 'torre', 'pecado', 'debate', 'cebra', 'aldea', 'orilla', 'tiempo', 'brazo', 'voz', 'cintura', 'disco', 'hormiga', 'coraje', 'feliz', 'catarro', 'miel', 'golpe', 'avion', 'frente', 'pluma', 'gol', 'saber', 'figura', 'guante', 'casa', 'mujer', 'diario', 'sol', 'antena', 'calle', 'cometa', 'cuervo', 'cuerpo', 'iglesia', 'sello', 'telar', 'zona', 'bolsillo', 'pena', 'capilla', 'serpiente', 'espejo', 'destino', 'lucha', 'alterar', 'puerto', 'rosa', 'elefante', 'canto', 'armario', 'cruz', 'caida', 'trenza', 'fama', 'caballo', 'joven', 'boca', 'barco', 'beber', 'secreto', 'corona', 'puente', 'tenis', 'actor', 'frio', 'moneda', 'clima', 'ladron', 'trueno', 'dedo', 'oceano', 'corazon', 'gracia', 'duende', 'tinta', 'dolor', 'acuerdo', 'aliento', 'fiera', 'burla', 'tumba', 'bateria', 'valle', 'tierra', 'billete', 'madre', 'teoria', 'estrella', 'ilusion', 'castillo', 'globo', 'rumor', 'cancer', 'creer', 'dama', 'mentira', 'orden', 'violeta', 'fuego', 'borde', 'jugador', 'animo', 'cuento', 'huella', 'fondo', 'altura', 'anhelo', 'amigo', 'esquina', 'oferta', 'paz', 'piedra', 'espuma', 'carrera', 'alcalde', 'roca', 'salto', 'bebida', 'derecho', 'isla', 'error', 'recuerdo', 'marea', 'gato', 'temor', 'calma', 'rio', 'sombrero', 'rayo', 'guerra', 'barril', 'faro', 'cerca', 'dinero', 'yerba', 'diamante', 'daño', 'broma', 'sueño', 'minuto', 'largo', 'amparo', 'causa', 'ciudad', 'fantasma', 'acento', 'luz', 'caja', 'diablo', 'cancion', 'papel', 'peso', 'cuadro', 'mundo', 'lider', 'reto', 'nieve', 'salud', 'acorde', 'bola', 'riesgo', 'trato', 'bocina', 'rico', 'rana', 'campo', 'alma', 'hierro', 'amante', 'sangre', 'espina', 'edad', 'claridad', 'tarde', 'gente', 'rojo', 'aprecio', 'avenida', 'niño', 'deseo', 'chispa', 'ruina', 'zorro', 'bloque', 'leon', 'perro', 'libro', 'caracter', 'anillo', 'escalera', 'fiesta', 'triangulo', 'culto', 'costa', 'lago', 'palacio', 'parte', 'agua', 'hacha', 'grano', 'blanco', 'premio', 'vuelo', 'crimen', 'hogar', 'rango', 'mar', 'aire', 'compra', 'tigre', 'diente', 'juego', 'idea', 'caricia', 'pacto', 'furia', 'teatro', 'zapato', 'carga', 'puño', 'volcan', 'cazador', 'barro', 'abismo', 'rey', 'cedro', 'velero', 'llama', 'magia', 'flor', 'mano', 'cola', 'noche', 'claro', 'dragon', 'ataque', 'herida', 'olvido', 'precio', 'ritmo', 'cadena', 'cielo', 'justicia', 'arte', 'extraño', 'pais', 'costa', 'paz', 'campo', 'orilla', 'seda', 'barco', 'cerca', 'idea', 'alma', 'valle', 'cedro', 'palacio', 'rayo', 'diablo', 'hormiga', 'aire', 'eco', 'carga', 'perro', 'oso', 'cielo', 'cielo', 'lider', 'palacio', 'flor', 'sombrero', 'cancion', 'reto', 'fondo', 'calma', 'guerra', 'mujer', 'lago', 'altura', 'antena', 'llama', 'caracter', 'carga', 'pared', 'papel', 'seda', 'ruido', 'vuelo', 'fiesta', 'acento', 'tigre', 'dedo', 'teatro', 'viento', 'minuto', 'guante', 'niño', 'dragon', 'piedra', 'herida', 'mujer', 'carrera', 'casa', 'pecado', 'puerto', 'zona', 'fantasma', 'gol', 'zorro', 'abismo', 'jabon', 'cola', 'extraño', 'ruido', 'deseo', 'caida', 'pecado', 'marea', 'gato', 'lucha', 'trenza', 'carrera', 'rosa', 'caballo', 'cedro', 'zona', 'cebra', 'yunque', 'lago', 'rey', 'huella', 'luz', 'piedra', 'tigre', 'caida', 'golpe', 'poder', 'guerra', 'vidrio', 'deseo', 'canto', 'cielo', 'animo', 'cuerpo', 'broma', 'ruido', 'gafas', 'ciudad', 'bola', 'yunque', 'teatro', 'saber', 'guerra', 'frio', 'billete', 'serpiente', 'acuerdo', 'cometa', 'olvido', 'diario', 'cancer', 'esquina', 'carrera', 'feliz', 'culto', 'gol', 'caida', 'extraño', 'valle', 'banda', 'paz', 'precio', 'serpiente', 'rana', 'tenis', 'vidrio', 'blanco', 'espina', 'capilla', 'capilla', 'riesgo', 'guerra', 'tarde', 'barril', 'cancer', 'templo', 'lider', 'cancion', 'casa', 'grano', 'minuto', 'cuadro', 'pacto', 'mano', 'claro', 'joven', 'lucha', 'dolor', 'cuento', 'mar', 'bateria', 'velero', 'sueño', 'canto', 'zapato', 'deseo', 'altura', 'actor', 'aliento', 'cerca', 'oso', 'creer', 'mentira', 'orilla', 'mano', 'esquina', 'diario', 'blanco', 'deseo', 'juego', 'hormiga', 'mar', 'velero', 'telar', 'figura', 'destino', 'mar', 'compra', 'mujer', 'disco', 'zorro', 'error', 'costa', 'idea', 'caballo', 'amante', 'cintura', 'lider', 'alma', 'sueño', 'oceano', 'bolsillo', 'cruz', 'figura', 'trueno', 'noche', 'trueno', 'caracter', 'ilusion', 'volcan', 'armario', 'lancha', 'costa', 'seda', 'pais', 'zona', 'calle', 'carne', 'telar', 'gracia', 'mundo', 'casa', 'diente']
    for p in palabras:
        lista_palabras= p.split()
    return  lista_palabras

#B
def elegir_palabra(listadepalabras:list[str])->str:
    ''' 
    Recibe una lista de palabras y devuelve una palabra elegida al azar.
    
    :param palabra: Lista de palabras
    :type palabra: list[str]
    :return: Una palabra elegida al azar de la lista
    :rtype: str
    '''
    return random.choice(listadepalabras)

#C
def enmascarar_palabra(palabra:str,letras_probadas:set[str])->str:
    ''' 
    Recibe una palabra y un conjunto de letras probadas y devuelve la palabra enmascarada.
    Las letras que no estén en el conjunto de letras probadas se reemplazan por guiones bajos.
    
    :param palabra: La palabra a enmascarar
    :type palabra: str
    :param letras_probadas: Conjunto de letras que se han probado
    :type letras_probadas: set[str]
    :return: La palabra enmascarada
    :rtype: str
    '''
    
    # 1. Creamos una lista para almacenar el resultado.
    #    Vamos a añadir las letras o los guiones uno por uno.
    resultado_parcial = [] 
    
    # 2. Recorremos la palabra secreta (el for separa automáticamente en letras los strings)
    for letra in palabra:
        
        if letra in letras_probadas:
            resultado_parcial.append(letra)
        else:
            resultado_parcial.append('_')
            
    return " ".join(resultado_parcial) 


#D
def pedir_letra(letras_probadas:set[str])->str:
    #Se pone un bucle para que siga pidiendo letra hasta que se introduzca una válida
    while True:
        letra_pedida = input("Adivina una letra: ").lower()
        
        if len(letra_pedida) != 1:
            print("Solo puedes introducir una letra. Intenta con otra: ")
        elif not letra_pedida.isalpha():
            print("Debes introducir un carácter alfabético. Intenta con otra: ")
        elif letra_pedida in letras_probadas:
            print("Ya has introducido esa letra antes. Intenta con otra: ")
        else:
            return letra_pedida # Es válida, salimos
        
#E
def comprobar_letra(palabra:str,letra:str)->bool:
    
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError("La letra debe ser un único carácter de tipo alfabético")
    elif letra in palabra:
        return True
    else:
        return False        
    
#F
def comprobar_palabra_completa(palabra:str,letras_probadas:set[str])->bool:
    for letra in palabra:
        if letra not in letras_probadas:
            return False
    return True

#G

        

    
    