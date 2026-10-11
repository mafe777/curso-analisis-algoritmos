"""Validación experimental y comparación entre Insertion Sort y Merge Sort"""

import time
import matplotlib.pyplot as plt
from datos import generar_aleatorio
from algoritmos import insertion_sort, merge_sort


def ejecutar_comparacion() -> None:
    """mide el tiempo de ejecucion de insertion_sort y merge_sort

    sobre el escenario A y genera la grafica comparativa en graficas/.
    """
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400]
    
    tiempos_insertion = []
    tiempos_merge = []

    for n in tamanios:
        datos = generar_aleatorio(n)

        # Medición Insertion Sort
        inicio = time.perf_counter()
        insertion_sort(datos)
        fin = time.perf_counter()
        tiempos_insertion.append(fin - inicio)

        # Medición Merge Sort
        inicio = time.perf_counter()
        merge_sort(datos)
        fin = time.perf_counter()
        tiempos_merge.append(fin - inicio)

    # Gráfica Parte 4: Tiempo vs. Tamaño de entrada (Ambos algoritmos)
    plt.figure(figsize=(8, 5))
    plt.plot(tamanios, tiempos_insertion, marker='o', label='Insertion Sort')
    plt.plot(tamanios, tiempos_merge, marker='s', label='Merge Sort')
    plt.title('Comparación de Tiempos: Insertion Sort vs. Merge Sort')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/parte4_tiempo.png')
    plt.close()


if __name__ == '__main__':
    ejecutar_comparacion()