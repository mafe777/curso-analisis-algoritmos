"""Script de experimentación y medición de tiempos para Fuerza Bruta vs Divide y Vencerás."""

import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_experimento() -> None:
    """Mide los tiempos de ejecución de ambos algoritmos y genera la gráfica comparativa."""
# Tamaños de entrada solicitados (incluyendo menores de 100 y 4000+)
    tamanios = [10, 50, 100, 500, 1000, 4000]
    
    tiempos_fb = []
    tiempos_dyv = []

    print("Iniciando mediciones de rendimiento...")
    for n in tamanios:
        # Generar datos con semilla fija y valores entre -100 y 100
        random.seed(42)
        valores = [random.uniform(-100, 100) for _ in range(n)]

        # Medir Fuerza Bruta
        inicio_fb = time.perf_counter()
        res_fb = subarreglo_fuerza_bruta(valores)
        fin_fb = time.perf_counter()
        tiempo_fb = fin_fb - inicio_fb

        # Medir Divide y Vencerás
        inicio_dyv = time.perf_counter()
        res_dyv = subarreglo_maximo(valores, 0, len(valores) - 1)
        fin_dyv = time.perf_counter()
        tiempo_dyv = fin_dyv - inicio_dyv

        # Verificar dentro del experimento que ambos dan la misma suma
        assert abs(res_fb[2] - res_dyv[2]) < 1e-5, f"Discrepancia en n={n}"

        tiempos_fb.append(tiempo_fb)
        tiempos_dyv.append(tiempo_dyv)
        print(f"n = {n:4d} | Fuerza Bruta: {tiempo_fb:.6f} s | Divide y Vencerás: {tiempo_dyv:.6f} s")

    # Generación de la gráfica con Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos_fb, marker='o', linestyle='-', color='crimson', label='Fuerza Bruta $\\Theta(n^2)$')
    plt.plot(tamanios, tiempos_dyv, marker='s', linestyle='-', color='dodgerblue', label='Divide y Vencerás $\\Theta(n \\log n)$')

    plt.title("Rendimiento: Subarreglo Máximo (Fuerza Bruta vs Divide y Vencerás)")
    plt.xlabel("Tamaño de entrada ($n$ días)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # Guardar en la ruta requerida dentro de la carpeta graficas/
    ruta_grafica = "lab2-divide-y-vencer/graficas/tiempo_vs_n.png"
    plt.savefig(ruta_grafica, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"\n¡Gráfica guardada exitosamente en '{ruta_grafica}'!")


if __name__ == "__main__":
    ejecutar_experimento()