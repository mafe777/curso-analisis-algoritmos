"""Script de experimentación y medición de tiempos para Lista Enlazada vs Tabla Hash."""

import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guías de diez dígitos que no están en la colección."""
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def ejecutar_experimentos() -> None:
    """Ejecuta los experimentos A y B, y genera las gráficas correspondientes."""
    
    # Asegurar que la carpeta de gráficas exista
    os.makedirs("lab3-estructuras-datos/graficas", exist_ok=True)
    
    # -------------------------------------------------------------
    # Experimento A: Lista vs Tabla Hash frente a n
    # -------------------------------------------------------------
    tamanios = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []

    print("Iniciando Experimento A (Lista vs Tabla Hash)...")
    for n in tamanios:
        azar = random.Random(42)
        claves = set()
        while len(claves) < n:
            claves.add(azar.randint(10**9, 10**10 - 1))
        
        lista = ListaEnlazada()
        m = max(3, int(n / 2))
        tabla = TablaHash(m)

        for guia in claves:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        inexistentes = generar_guias_inexistentes(claves, 200, semilla=7)

        # Medir búsqueda en lista enlazada
        inicio_l = time.perf_counter()
        for g in inexistentes:
            lista.buscar(g)
        fin_l = time.perf_counter()
        tiempo_medio_lista = (fin_l - inicio_l) / 200

        # Medir búsqueda en tabla hash
        inicio_t = time.perf_counter()
        for g in inexistentes:
            tabla.buscar(g)
        fin_t = time.perf_counter()
        tiempo_medio_tabla = (fin_t - inicio_t) / 200

        tiempos_lista.append(tiempo_medio_lista)
        tiempos_tabla.append(tiempo_medio_tabla)
        print(f"n = {n:5d} | m = {m:5d} | Lista: {tiempo_medio_lista:.8f} s | Tabla: {tiempo_medio_tabla:.8f} s")

    # Gráfica Experimento A
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos_lista, marker='o', linestyle='-', color='crimson', label='Lista Enlazada $\\Theta(n)$')
    plt.plot(tamanios, tiempos_tabla, marker='s', linestyle='-', color='dodgerblue', label='Tabla Hash $\\Theta(1 + \\alpha)$')
    plt.title("Rendimiento: Lista Enlazada vs Tabla Hash (Búsquedas Inexistentes)")
    plt.xlabel("Número de guías ($n$)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("lab3-estructuras-datos/graficas/lista_vs_tabla.png", dpi=300, bbox_inches='tight')
    plt.close()

    # -------------------------------------------------------------
    # Experimento B: Efecto del factor de carga (alfa) con n fijo
    # -------------------------------------------------------------
    n_fijo = 20000
    alfas_objetivo = [0.25, 1.0, 4.0, 10.0]
    valores_alfa = []
    tiempos_alfa = []

    print("\nIniciando Experimento B (Efecto del factor de carga)...")
    azar = random.Random(42)
    claves_fijas = set()
    while len(claves_fijas) < n_fijo:
        claves_fijas.add(azar.randint(10**9, 10**10 - 1))

    inexistentes_b = generar_guias_inexistentes(claves_fijas, 200, semilla=7)

    for alfa_obj in alfas_objetivo:
        m_val = max(1, int(n_fijo / alfa_obj))
        tabla_b = TablaHash(m_val)
        for guia in claves_fijas:
            tabla_b.insertar(guia, "en reparto")

        alpha_real = tabla_b.factor_carga()

        inicio_b = time.perf_counter()
        for g in inexistentes_b:
            tabla_b.buscar(g)
        fin_b = time.perf_counter()
        tiempo_medio_b = (fin_b - inicio_b) / 200

        valores_alfa.append(alpha_real)
        tiempos_alfa.append(tiempo_medio_b)
        print(f"Alfa objetivo: {alfa_obj:4.2f} | Alfa real: {alpha_real:5.2f} | m: {m_val:6d} | Tiempo: {tiempo_medio_b:.8f} s")

    # Gráfica Experimento B
    plt.figure(figsize=(10, 6))
    plt.plot(valores_alfa, tiempos_alfa, marker='^', linestyle='-', color='forestgreen', label='Tabla Hash')
    plt.title("Efecto del Factor de Carga ($\\alpha$) en el Tiempo de Búsqueda")
    plt.xlabel("Factor de carga ($\\alpha = n / m$)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("lab3-estructuras-datos/graficas/tiempo_vs_alfa.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("\n¡Experimentos completados y gráficas generadas con éxito!")


if __name__ == "__main__":
    ejecutar_experimentos()