# 🚀 Proyecto de Laboratorio: Calculadora de Viajes Espaciales

**Autor**: Fermín L. Cruz  **Fecha última modificación**: 24/09/2025


¡Prepárate para una misión interplanetaria! En este laboratorio vas a construir una serie de scripts que simulan distintos aspectos de una misión espacial: cálculos de viaje, condiciones para realizar el viaje, y más.

---

## ⏱ Duración estimada

2 horas

---

## ✅ ¿Qué se practica?

- Tipos de datos: `float`, `int`, `str`, `bool`
- Entrada y salida
- Expresiones y operadores
- Condicionales `if` / `else`
- Bucles `for` con `range()`
- Bucles `while`

---

## 📁 Archivos del proyecto

Debes crear los siguientes módulos en la carpeta `src`:

| Archivo           | Qué se hace                                                 |
|-------------------|-------------------------------------------------------------|
| `viaje_ej1.py`       | Calcular duración de viaje en días                          |
| `viaje_ej2.py`       | Entrada del usuario (distancia y velocidad)                 |
| `viaje_ej3.py`       | Comprobar si puedes embarcarte en la misión                 |
| `viaje_ej4.py`       | Tabla de tiempos para distintas velocidades (`for`)         |
| `viaje_ej5.py`       | Repetir simulaciones con `while`                            |
| `viaje_extra1.py`  | Simulación de repostaje en ruta                             |
| `viaje_extra2.py` | Cálculo de semanas y días                                   |

---

## 📌 Ejercicio 1: Tiempo de viaje (`viaje_ej1.py`)

Calcula cuántos días tardarías en recorrer una distancia si viajas a cierta velocidad. Crea un fichero `viaje_ej1.py` en la carpeta `src` y copia dentro el siguiente código:

```python
distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")
```

Ejecuta el programa y observa la salida en el terminal.

Ahora cambia esta línea:

```python
tiempo_dias = tiempo_horas / 24
```

por esta otra:

```python
tiempo_dias = tiempo_horas // 24
```

¿Qué ha ocurrido? Prueba también a cambiar esta línea:

```python
tiempo_horas = distancia_km / velocidad_kmh
```

por esta otra:

```python
tiempo_horas = distancia_km // velocidad_kmh
```

¿Sabrías explicar por qué a veces se muestran números decimales y otras veces no?

---

## 📌 Ejercicio 2: Entrada del usuario (`viaje_ej2.py`)

Copia el código del ejercicio anterior, y modifícalo para que se le pida al usuario la distancia y la velocidad mediante `input()`. Recuerda que debes convertir los valores leídos a `int`.

---

## 📌 Ejercicio 3: ¿Puedes viajar? (`viaje_ej3.py`)

Pide la **edad** y el **nivel físico** (de 1 a 10) del usuario. Usa `if` para decidir si puede embarcarse, siguiendo estas reglas:

- Edad < 18 → "Debes ser mayor de edad."
- Nivel físico < 5 → "Debes estar en mejor forma."
- Si cumple ambas: "¡Listo para despegar!"

¿Cómo podríamos evitar que el usuario no introduzca un valor fuera del rango permitido (de 1 a 10) para su nivel físico?

---

## 📌 Ejercicio 4: Tabla de tiempos (`viaje_ej4.py`)

Muestra cuánto se tarda en llegar a Marte (225 millones de km) con velocidades de 10.000 a 50.000 km/h (en saltos de 10.000 km/h), usando `for` y `range()`:

```python
# Salida esperada:
Velocidad: 10000 km/h -> Tiempo: 937.5 días
Velocidad: 20000 km/h -> Tiempo: 468.75 días
...
```

---

## 📌 Ejercicio 5: Repetir simulaciones (`viaje_ej5.py`)

Haz que el usuario pueda repetir todo el cálculo de `viaje_ej2.py`, preguntándole después si quiere hacer otra simulación (`s/n`). Es decir, el flujo de ejecución será el siguiente:

1. Pide al usuario la distancia y la velocidad.
2. Calcula y muestra el tiempo de viaje.
3. Pregunta: "¿Quieres hacer otra simulación? (s/n)"
4. Si responde "s", repite desde el paso 1. Si responde "n", termina el programa.

---

## ⭐ Ejercicio extra: Simulación de repostaje en ruta (`viaje_extra1.py`)

Imagina que tu nave solo puede recorrer **150.000 km** antes de necesitar repostar. Escribe un programa que calcule:

- Cuántas paradas de repostaje necesitas para llegar a un destino (pide la distancia al usuario).
- Muestra por pantalla en qué kilómetros tendrás que parar a repostar (por ejemplo: "Parada en el km 150000", "Parada en el km 300000", etc.).
- Al final, indica el número total de paradas para repostar.

**Pista:** Usa un bucle `while` o `for` para calcular las paradas.

```python
# Salida esperada:
Introduce la distancia total en km: 500000
Parada en el km 150000
Parada en el km 300000
Parada en el km 450000
Total de paradas para respostar: 3
```

---

## ⭐ Ejercicio extra: Calculo de semanas y días (`viaje_extra2.py`) 

Adapta todos los ejercicios en los que se muestran días para mostrar semanas y días. Por ejemplo, en lugar de mostrar "16 días", se mostraría "2 semanas y 2 días".

---
---

**NOTA IMPORTANTE**: En el desarrollo de los ejercicios, habrás observado que hemos repetido en varias ocasiones algunos conjuntos de instrucciones (por ejemplo, para el cálculo del tiempo de viaje). Esto es algo que debe evitarse si queremos obtener programas fáciles de mantener y de extender. Veremos más adelante cómo evitar este problema mediante el uso de funciones.
