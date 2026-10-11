"""Experimentos para la Parte 3: Peor caso, mejor caso y caso promedio"""

import time
import matplotlib.pyplot as plt
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso
from algoritmos import insertion_sort


def ejecutar_experimento() -> None:
    """Ejecuta insertion sort en los tres escenarios, mide tiempos y comparaciones,

    y genera las gráficas correspondientes en la carpeta graficas/.
    """
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400]
    
    tiempos_a = []
    tiempos_b = []
    tiempos_c = []
    
    comps_a = []
    comps_b = []
    comps_c = []

    for n in tamanios:
        # Escenario A: Aleatorio
        datos_a = generar_aleatorio(n)
        inicio = time.perf_counter()
        _, c_a = insertion_sort(datos_a)
        fin = time.perf_counter()
        tiempos_a.append(fin - inicio)
        comps_a.append(c_a)

        # Escenario B: Casi ordenado
        datos_b = generar_casi_ordenado(n)
        inicio = time.perf_counter()
        _, c_b = insertion_sort(datos_b)
        fin = time.perf_counter()
        tiempos_b.append(fin - inicio)
        comps_b.append(c_b)

        # Escenario C: Orden inverso
        datos_c = generar_inverso(n)
        inicio = time.perf_counter()
        _, c_c = insertion_sort(datos_c)
        fin = time.perf_counter()
        tiempos_c.append(fin - inicio)
        comps_c.append(c_c)

    # Gráfica 1: Comparaciones vs. Tamaño de entrada
    plt.figure(figsize=(8, 5))
    plt.plot(tamanios, comps_a, marker='o', label='Escenario A (Aleatorio)')
    plt.plot(tamanios, comps_b, marker='s', label='Escenario B (Casi ordenado)')
    plt.plot(tamanios, comps_c, marker='^', label='Escenario C (Inverso)')
    plt.title('Insertion Sort: Comparaciones por Escenario')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Número de comparaciones')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/parte3_comparaciones.png')
    plt.close()

    # Gráfica 2: Tiempo vs. Tamaño de entrada
    plt.figure(figsize=(8, 5))
    plt.plot(tamanios, tiempos_a, marker='o', label='Escenario A (Aleatorio)')
    plt.plot(tamanios, tiempos_b, marker='s', label='Escenario B (Casi ordenado)')
    plt.plot(tamanios, tiempos_c, marker='^', label='Escenario C (Inverso)')
    plt.title('Insertion Sort: Tiempo de Ejecución por Escenario')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/parte3_tiempo.png')
    plt.close()


if __name__ == '__main__':
    ejecutar_experimento()