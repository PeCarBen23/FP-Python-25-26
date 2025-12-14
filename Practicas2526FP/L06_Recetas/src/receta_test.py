from recetas import *

def test_lee_recetas(recetas: list[Receta]) -> None:
    print("\ntest_lee_recetas")
    print(f"Registros leídos: {len(recetas)}")
    print(f"Los dos primeros: {recetas[:2]}")
    print(f"\nLos dos últimos: {recetas[-2:]}")

# def test_diferentes_ingredientes(recetas: list[Receta], unidad: str) -> None:
#     print("\ntest_diferentes_ingredientes")
#     print(f"Los diferentes ingredientes que se miden en {unidad} son: {diferentes_ingredientes(recetas, unidad)}")

# def test_recetas_con_ingredientes(recetas: list[Receta], ingredientes: set[str]) -> None:
#     print("\ntest_recetas_con_ingredientes")
#     print(f"Las recetas con alguno de los siguientes ingredientes {ingredientes} son: {recetas_con_ingredientes(recetas, ingredientes)}")

# def test_receta_más_barata(recetas: list[Receta], tipos: set[str], n: int | None = None) -> None:
#     print("\ntest_receta_más_barata")
#     print(f"La receta más barata de las {n} con menos calorías de los siguientes tipos {tipos} es: {receta_más_barata(recetas, tipos, n)}")

# def test_recetas_con_más_ingredientes_y_más_caras(recetas: list[Receta], ingredientes: set[Ingrediente]) -> None:
#     print("\ntest_recetas_con_más_ingredientes_y_más_caras")
#     for r in recetas_con_más_ingredientes_y_más_caras(recetas, ingredientes):
#         print(f"Denominación: {r.denominación}, número ingredientes: {len(r.ingredientes)} y precio: {r.precio}")

if __name__ == '__main__':
    recetas = lee_recetas("Practicas2526FP/Practicas2526FP/L06_Recetas/src/recetas.csv")

    # Descomentar las siguientes líneas para ejecutar las pruebas

    test_lee_recetas(recetas)
    # test_diferentes_ingredientes(recetas, "gr")
    # test_diferentes_ingredientes(recetas, "cl")
    # test_recetas_con_ingredientes(recetas, {"azúcar", "harina"})
    # test_recetas_con_ingredientes(recetas, {"cebolla", "tomate", "pimiento"})
    # test_receta_más_barata(recetas, {'Postre', 'Entrante'})
    # test_receta_más_barata(recetas, {'Plato Principal', 'Postre'}, 5)
