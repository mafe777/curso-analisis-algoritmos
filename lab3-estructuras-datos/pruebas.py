"""Script de pruebas unitarias para la lista enlazada y la tabla hash."""

import random
from estructuras import ListaEnlazada, TablaHash

# 1. Búsqueda exitosa e infructuosa en la lista enlazada
lista = ListaEnlazada()
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")
assert lista.buscar(1000000010) == "en bodega"
assert lista.buscar(9999999999) is None

# 2. Búsqueda exitosa e infructuosa en la tabla hash
tabla_prueba = TablaHash(10)
tabla_prueba.insertar(1000000010, "en bodega")
assert tabla_prueba.buscar(1000000010) == "en bodega"
assert tabla_prueba.buscar(9999999999) is None

# 3. Colisión forzada: con m = 7, las guías 10, 24 y 17 caen en la casilla 3
tabla_colision = TablaHash(7)
for guia in (10, 24, 17):
    tabla_colision.insertar(guia, "en bodega")

assert tabla_colision.buscar(10) == "en bodega"
assert tabla_colision.buscar(24) == "en bodega"
assert tabla_colision.buscar(17) == "en bodega"

# Verificar que la lista de esa casilla tiene longitud 3
assert tabla_colision.casillas[3].tamano == 3

# 4. Verificar que factor_carga() da 3 / 7
assert abs(tabla_colision.factor_carga() - (3 / 7)) < 1e-5

# 5. Al menos veinte colecciones aleatorias comparando la lista y la tabla
random.seed(42)
for _ in range(20):
    m = random.choice([5, 7, 11, 13, 17])
    t = TablaHash(m)
    l = ListaEnlazada()
    
    claves = [random.randint(10**9, 10**10 - 1) for _ in range(15)]
    estados = ["en bodega", "en reparto", "entregado"]
    
    for k in claves:
        est = random.choice(estados)
        t.insertar(k, est)
        l.insertar(k, est)
        
    # Validar búsqueda de claves existentes
    for k in claves:
        assert t.buscar(k) == l.buscar(k)
        
    # Validar búsqueda de una clave inexistente
    inexistente = 8888888888
    assert t.buscar(inexistente) is None
    assert l.buscar(inexistente) is None

print("¡Todas las pruebas pasaron con éxito!")

if __name__ == "__main__":
    pass