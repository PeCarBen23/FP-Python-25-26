# Proyecto L06_Recetas

### Condiciones Iniciales:
Se facilita una carpeta **data** con el fichero denominado ``recetas.csv`` con datos sobre recetas culinarias. Ábralo para ver su estructura. 

Cree una carpeta **src** para incluir los siguientes módulos Python:

**receta.py** en el que implemente las funciones que se indican a continuación.

**test_receta.py** en el que incluirá las sentencias necesarias para ir probando las funciones a medida que las implemente.

La información de cada registro del fichero es la que se indica a continuación. **Observe en el fichero que los ingredientes están compuestos por tres campos y que a alguna receta le faltan los ingredientes**.
```
• denominación:  denominación de la receta.
• tipo: tipo de receta (Postre, Plato principal etc).
• dificultad: dificultad de elaboración (Baja, Media, Alta).
• ingredientes: ingredientes de la receta. Cada ingrediente lleva su nombre, la cantidad y las unidades con las que se confecciona la receta (u=unidades/gr=gramos/cl=centilitros)
• tiempo de preparación: tiempo de elaboración en minutos.
• calorías: número de calorías de una porción.
• fecha de creación: fecha en la que se añadió la receta al dataset.
• precio estimado: precio por persona.
```

### Ejercicio 1

Copie en receta.py los siguientes NamedTuple e importe los tipos y funciones que necesite:
```
Ingrediente = NamedTuple("Ingrediente",
					     [("nombre",str),
						  ("cantidad",float),
						  ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominación", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", Optional[list[Ingrediente]]),
                     ("tiempo", int),
                     ("calorías", int),
                     ("fecha", date),
                     ("precio", float)])

```
### Ejercicio 2
Defina una función ``lee_recetas`` que reciba como parámetro el nombre de un fichero con la estructura de ``recetas.csv`` y devuelva una lista de tuplas de tipo **Receta** con los registros leídos del fichero.

Resultados esperados en el test:
```
test_lee_recetas
Registros leídos: 30
Los dos primeros: [Receta(denominación='Ensalada de Frutas', tipo='Postre', dificultad='Baja', ingredientes=[Ingrediente(nombre='fresas', cantidad=5.0, unidad='u'), Ingrediente(nombre='piña', cantidad=0.25, unidad='u'), Ingrediente(nombre='kiwi', cantidad=1.0, unidad='u'), Ingrediente(nombre='menta', cantidad=50.0, unidad='cl'), 
Ingrediente(nombre='zumo naranja', cantidad=100.0, unidad='cl')], tiempo=15, calorías=120, fecha=datetime.date(2024, 1, 14), precio=7.5), Receta(denominación='Spaghetti Bolognese', tipo='Plato principal', dificultad='Media', ingredientes=[Ingrediente(nombre='pasta', cantidad=200.0, unidad='gr'), Ingrediente(nombre='carne picada', cantidad=250.0, unidad='gr'), Ingrediente(nombre='tomate frito', cantidad=150.0, unidad='gr'), Ingrediente(nombre='cebolla', cantidad=0.5, unidad='u'), Ingrediente(nombre='dientes ajo', cantidad=4.0, unidad='u')], tiempo=45, calorías=400, fecha=datetime.date(2024, 1, 9), precio=12.5)]

Los dos últimos: [Receta(denominación='Sopa de Champiñones', tipo='Entrante', dificultad='Baja', ingredientes=[Ingrediente(nombre='champiñones', cantidad=200.0, unidad='gr'), Ingrediente(nombre='cebolla', cantidad=0.75, unidad='u'), Ingrediente(nombre='dientes ajo', cantidad=3.0, unidad='u'), Ingrediente(nombre='caldo de pollo', 
cantidad=500.0, unidad='cl'), Ingrediente(nombre='perejil', cantidad=10.0, unidad='gr')], tiempo=30, calorías=180, fecha=datetime.date(2024, 2, 27), precio=8.5), Receta(denominación='Arroz con Pollo', tipo='Plato principal', dificultad='Baja', ingredientes=[Ingrediente(nombre='arroz', cantidad=150.0, unidad='gr'), Ingrediente(nombre='pollo', cantidad=1.0, unidad='u'), Ingrediente(nombre='cebolla', cantidad=1.0, unidad='u'), Ingrediente(nombre='pimiento', cantidad=1.0, unidad='u'), Ingrediente(nombre='azafrán', cantidad=5.0, unidad='gr')], tiempo=40, calorías=380, fecha=datetime.date(2024, 2, 6), precio=14.99)]
```
### Ejercicio 3
Defina una función ``diferentes_ingredientes`` que reciba como parámetros una lista de tipo Receta y una unidad de medidas de los ingredientes de tipo str, que puede tomar el valor **None**, en cuyo caso no se filtra por unidad y devuelva el número de los diferentes ingredientes que se han medido en la unidad dada.

Resultados esperados en el test:
```
test_diferentes_ingredientes
Los diferentes ingredientes que se miden en gr son: 33

test_diferentes_ingredientes
Los diferentes ingredientes que se miden en cl son: 12
```
### Ejercicio 4
Defina una función ``recetas_con_ingredientes`` que reciba como parámetros una lista de tipo Receta, un conjunto con nombres de ingredientes y devuelva una lista de tuplas con las denominaciones, las calorías y los precios de las recetas que entre sus ingredientes existe alguno de los dados como parámetro. La lista debe estar ordenada de mayor a menor precio. 

**Nota** Tenga en cuenta que si la receta tiene más de uno de los ingredientes dados, solo debe aparecer una vez.

Resultados esperados en el test:
```
test_recetas_con_ingredientes
Las recetas con alguno de los siguiente ingredientes {'azúcar', 'harina'} son: [('Pastel de Zanahoria', 300, 13.5), ('Mousse de Chocolate', 300, 9.5), ('Galletas de Avena', 150, 7.95), ('Muffins de Arándanos', 180, 7.95)]

test_recetas_con_ingredientes
Las recetas con alguno de los siguiente ingredientes {'pimiento', 'cebolla', 'tomate'} son: [('Pollo al Curry', 400, 15.75), ('Arroz con Pollo', 380, 14.99), ('Risotto de Champiñones', 320, 13.99), ('Spaghetti Bolognese', 400, 12.5), ('Hamburguesa con Queso', 400, 11.25), ('Tortilla Española', 320, 11.25), ('Caponata', 160, 9.99), ('Sopa de Calabaza', 150, 9.95), ('Ensalada de Atún', 180, 9.25), ('Sopa de Tomate', 120, 8.5), ('Sopa de Champiñones', 180, 8.5), ('Gazpacho Andaluz', 150, 7.95), ('Bruschetta', 160, 7.25)]
```

### Ejercicio 5
Defina una función ``receta_más_barata`` que reciba como parámetros una lista de tipo Receta, un conjunto con tipos de recetas y un parámetro "n" de tipo entero con valor por defecto **None**, y que devuelva la receta más barata (de menor importe) de entre las "n" recetas con menos calorías (las que menos engordan) de alguno de los tipos de receta dados como parámetro.
Si n toma el valor **None** se buscará la receta más barata de entre totas las recetas.

**Ayuda:** Primero obtenga las n-recetas que menos engordan y de ellas busque la más barata.

Resultados esperados en el test:
```
test_receta_más_barata
La receta más barata de que las None con menos calorías de los siguientes tipos {'Postre', 'Entrante'} es: Receta(denominación='Gazpacho', tipo='Entrante', dificultad='Baja', ingredientes=[], tiempo=25, calorías=120, fecha=datetime.date(2024, 2, 10), precio=6.95)

test_receta_más_barata
La receta más barata de que las 5 con menos calorías de los siguientes tipos {'Postre', 'Plato Principal'} es: Receta(denominación='Ensalada de Frutas', tipo='Postre', dificultad='Baja', ingredientes=[Ingrediente(nombre='fresas', cantidad=5.0, unidad='u'), Ingrediente(nombre='piña', cantidad=0.25, unidad='u'), Ingrediente(nombre='kiwi', cantidad=1.0, unidad='u'), Ingrediente(nombre='menta', cantidad=50.0, unidad='cl'), Ingrediente(nombre='zumo naranja', cantidad=100.0, unidad='cl')], tiempo=15, calorías=120, fecha=datetime.date(2024, 1, 14), precio=7.5)
```
### Ejercicio 6
Defina una función ``recetas_con_más_ingredientes_y_más_cara`` que reciba como parámetros una lista de tipo Receta, un conjunto de tipo ingrediente y que devuelva una lista de recetas ordenadas por  número de ingredientes y en caso de empate, desempaten por el precio.

**Ayuda:** El parámetro ``key`` en un sort, sorted, máx o min admite como criterio de ordenación una tupla. En este caso, aplica el criterio al primer elemento de la tupla, en caso de empate, lo aplica al segundo elemento y así sucesivamente.

Resultados esperados en el test:
```
test_recetas_con_más_ingredientes_y_más_cara
Denominación: Risotto de Champiñones, número ingredientes: 6 y precio: 13.99
Denominación: Ensalada de Atún, número ingredientes: 6 y precio: 9.25
Denominación: Pollo al Curry, número ingredientes: 5 y precio: 15.75
Denominación: Arroz con Pollo, número ingredientes: 5 y precio: 14.99
Denominación: Spaghetti Bolognese, número ingredientes: 5 y precio: 12.5
Denominación: Tortilla Española, número ingredientes: 5 y precio: 11.25
Denominación: Sopa de Calabaza, número ingredientes: 5 y precio: 9.95
Denominación: Mousse de Chocolate, número ingredientes: 5 y precio: 9.5
Denominación: Sopa de Tomate, número ingredientes: 5 y precio: 8.5
Denominación: Sopa de Champiñones, número ingredientes: 5 y precio: 8.5
Denominación: Galletas de Avena, número ingredientes: 5 y precio: 7.95
Denominación: Muffins de Arándanos, número ingredientes: 5 y precio: 7.95
Denominación: Pastel de Zanahoria, número ingredientes: 4 y precio: 13.5
```