"""Script para la medición de tiempos y generación de gráficas de rendimiento."""

import time
import random
import matplotlib.pyplot as plt
from subarreglo import subarreglo_maximo_dv, subarreglo_fuerza_bruta


def ejecutar_experimento() -> None:
    """mide tiempos de ejecución y genera la gráfica comparativa."""
    tamanios = [50, 100, 500, 1000, 2000, 4000]
    tiempos_fb = []
    tiempos_dv = []

    random.seed(42)

    for n in tamanios:
        datos = [random.randint(-100, 100) for _ in range(n)]

        inicio_fb = time.perf_counter()
        for _ in range(3):
            subarreglo_fuerza_bruta(datos)
        fin_fb = time.perf_counter()
        tiempos_fb.append((fin_fb - inicio_fb) / 3)

        inicio_dv = time.perf_counter()
        for _ in range(3):
            subarreglo_maximo_dv(datos, 0, len(datos) - 1)
        fin_dv = time.perf_counter()
        tiempos_dv.append((fin_dv - inicio_dv) / 3)

    plt.figure(figsize=(8, 5))
    plt.plot(tamanios, tiempos_fb, label="Fuerza Bruta O(n^2)", marker="o")
    plt.plot(tamanios, tiempos_dv, label="Divide y Vencerás O(n log n)", marker="s")
    plt.title("Comparativa de Rendimiento: Subarreglo Máximo")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución promedio (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("lab2-divide-y-vencer/graficas/rendimiento_dv.png")
    print("Gráfica generada y guardada exitosamente en lab2-divide-y-vencer/graficas/rendimiento_dv.png")


if __name__ == "__main__":
    ejecutar_experimento()