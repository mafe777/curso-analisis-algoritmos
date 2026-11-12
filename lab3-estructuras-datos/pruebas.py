"""Script de pruebas unitarias y validacion para las estructuras del Lab 03."""

import random
from estructuras import ListaEnlazada, TablaHash


def ejecutar_pruebas() -> None:
    """Ejecuta las pruebas requeridas para verificar la correctitud."""
    print("--- Ejecutando pruebas unitarias de Listas y Tablas Hash ---")

    # 1. Pruebas basicas de busqueda exitosa e infructuosa
    tabla = TablaHash(7)
    lista = ListaEnlazada()
    
    for g, e in [(100, "en bodega"), (200, "en reparto")]:
        tabla.insertar(g, e)
        lista.insertar(g, e)

    assert tabla.buscar(100) == "en bodega"
    assert tabla.buscar(999) is None
    assert lista.buscar(200) == "en reparto"
    assert lista.buscar(999) is None

    # 2. Colision forzada con m = 7 (guias 10, 24 y 17 caen en casilla 3)
    tabla_colision = TablaHash(7)
    for guia in (10, 24, 17):
        tabla_colision.insertar(guia, "en bodega")

    assert tabla_colision.buscar(24) == "en bodega"
    assert tabla_colision.buscar(99) is None
    assert tabla_colision.factor_carga() == 3 / 7
    assert tabla_colision.casillas[3].tamano == 3
    print("Prueba de colision forzada y factor de carga (3/7): OK")

    # 3. Veinte colecciones aleatorias comparando lista vs tabla hash
    random.seed(42)
    for i in range(20):
        tamanio = random.randint(10, 50)
        l_test = ListaEnlazada()
        t_test = TablaHash(5)  
        
        guias_insertadas = []
        for _ in range(tamanio):
            g = random.randint(10**8, 10**9 - 1)
            guias_insertadas.append(g)
            l_test.insertar(g, "activo")
            t_test.insertar(g, "activo")

        # Verificar busquedas exitosas
        for g in guias_insertadas:
            assert l_test.buscar(g) == t_test.buscar(g)

        # Verificar busquedas infructuosas
        for _ in range(5):
            g_inexistente = random.randint(10**10, 10**11 - 1)
            assert l_test.buscar(g_inexistente) == t_test.buscar(g_inexistente)

    print("¡Las 20 colecciones aleatorias pasaron con exito!")


if __name__ == "__main__":
    ejecutar_pruebas()