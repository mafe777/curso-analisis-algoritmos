"""Script de pruebas unitarias y validación para el Laboratorio 02."""

import random
from subarreglo import subarreglo_maximo_dv, subarreglo_fuerza_bruta


def ejecutar_pruebas() -> None:
    """Ejecuta casos de prueba específicos y aleatorios."""
    casos = [
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [8, -3, -5, 9, -2, -6, 1, 5],
        [10],
    ]

    print("--- Ejecutando pruebas unitarias ---")
    for idx, caso in enumerate(casos):
        res_fb = subarreglo_fuerza_bruta(caso)
        res_dv = subarreglo_maximo_dv(caso, 0, len(caso) - 1)
        print(f"Caso {idx + 1}: FB={res_fb[0]} | DV={res_dv[0]} -> Correcto: {res_fb[0] == res_dv[0]}")

    print("\n--- Verificando 20 listas aleatorias con enteros (-100 a 100) ---")
    for i in range(20):
        tamanio = random.randint(5, 50)
        lista_aleatoria = [random.randint(-100, 100) for _ in range(tamanio)]
        
        res_fb = subarreglo_fuerza_bruta(lista_aleatoria)
        res_dv = subarreglo_maximo_dv(lista_aleatoria, 0, len(lista_aleatoria) - 1)
        
        if res_fb[0] != res_dv[0]:
            print(f"Error en prueba aleatoria {i}: FB={res_fb[0]} vs DV={res_dv[0]}")
            return

    print("¡Todas las pruebas aleatorias pasaron con éxito!")


if __name__ == "__main__":
    ejecutar_pruebas()