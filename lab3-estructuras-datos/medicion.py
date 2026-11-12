"""Script para medir tiempos de busqueda y generar graficas de rendimiento."""

import time
import random
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen al conjunto.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(num: int) -> bool:
    """Verifica si un numero entero es primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def obtener_primo_cercano(n: int) -> int:
    """Encuentra un numero primo cercano a n / 2."""
    candidato = max(3, n // 2)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def ejecutar_experimentos() -> None:
    """Ejecuta el Experimento A y Experimento B generando las graficas."""
    print("--- Iniciando Experimento A: Lista vs Tabla Hash ---")
    tamanios = [100, 500, 1000, 5000, 10000, 20000]
    tiempos_lista = []
    tiempos_tabla = []

    for n in tamanios:
        # Construccion de datos con semilla fija
        azar = random.Random(42)
        existentes_set = set()
        lista = ListaEnlazada()
        m = obtener_primo_cercano(n)
        tabla = TablaHash(m)

        for _ in range(n):
            g = azar.randint(10**9, 10**10 - 1)
            existentes_set.add(g)
            lista.insertar(g, "en bodega")
            tabla.insertar(g, "en bodega")

        # Validacion previa obligatoria con assert para muestras existentes
        muestra_existente = list(existentes_set)[:5]
        for g in muestra_existente:
            assert lista.buscar(g) == tabla.buscar(g)

        # Generar guias inexistentes para medir el peor caso
        inexistentes = generar_guias_inexistentes(existentes_set, 200, semilla=7)

        # Medicion Lista Enlazada
        inicio = time.perf_counter()
        for g in inexistentes:
            lista.buscar(g)
        fin = time.perf_counter()
        tiempos_lista.append((fin - inicio) / len(inexistentes))

        # Medicion Tabla Hash
        inicio = time.perf_counter()
        for g in inexistentes:
            tabla.buscar(g)
        fin = time.perf_counter()
        tiempos_tabla.append((fin - inicio) / len(inexistentes))

    # Grafica Experimento A
    plt.figure(figsize=(8, 5))
    plt.plot(tamanios, tiempos_lista, label="Lista Enlazada O(n)", marker="o")
    plt.plot(tamanios, tiempos_tabla, label="Tabla Hash O(1 + alpha)", marker="s")
    plt.title("Experimento A: Tiempo Medio de Busqueda vs Numero de Guias (n)")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/lista_vs_tabla.png")
    plt.close()

    print("--- Iniciando Experimento B: Efecto del Factor de Carga (alpha) ---")
    n_fijo = 20000
    # Factores de carga objetivo entre 0.25 y 10
    alphas_objetivo = [0.25, 0.5, 1.0, 2.0, 5.0, 10.0]
    tiempos_alfa = []
    valores_alfa_reales = []

    azar_b = random.Random(42)
    existentes_b = set()
    guias_b = []
    for _ in range(n_fijo):
        g = azar_b.randint(10**9, 10**10 - 1)
        existentes_b.add(g)
        guias_b.append(g)

    inexistentes_b = generar_guias_inexistentes(existentes_b, 200, semilla=99)

    for alpha_obj in alphas_objetivo:
        m_calc = max(1, int(n_fijo / alpha_obj))
        tabla_b = TablaHash(m_calc)
        for g in guias_b:
            tabla_b.insertar(g, "en reparto")

        alpha_real = tabla_b.factor_carga()
        valores_alfa_reales.append(alpha_real)

        inicio = time.perf_counter()
        for g in inexistentes_b:
            tabla_b.buscar(g)
        fin = time.perf_counter()
        tiempos_alfa.append((fin - inicio) / len(inexistentes_b))

    # Grafica Experimento B
    plt.figure(figsize=(8, 5))
    plt.plot(valores_alfa_reales, tiempos_alfa, label="Tabla Hash (Busqueda Infructuosa)", marker="^", color="purple")
    plt.title("Experimento B: Tiempo Medio de Busqueda vs Factor de Carga (alpha)")
    plt.xlabel("Factor de carga (alpha = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/tiempo_vs_alfa.png")
    plt.close()
    print("¡Experimentos concluidos y graficas generadas en graficas/!")


if __name__ == "__main__":
    experimento = ejecutar_experimentos()