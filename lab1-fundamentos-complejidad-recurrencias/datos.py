"""Generadores de lotes de registros para los escenarios de Tamiza"""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A)

    Args:
        n: cantidad de registros del lote
        semilla: semilla del generador aleatorio

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada
    """
    random.seed(semilla)
    return random.sample(range(n * 10), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B)

    Args:
        n: cantidad de registros del lote
        semilla: semilla del generador aleatorio

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% ordenado y el 2% restante desordenado al final
    """
    random.seed(semilla)
    n_ordenado = int(n * 0.98)
    
    base = random.sample(range(n * 10), n)
    base.sort(reverse=True)
    
    parte_ordenada = base[:n_ordenado]
    parte_desordenada = base[n_ordenado:]
    random.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C)

    Args:
        n: cantidad de registros del lote

    Returns:
        Lista de n indices de riesgo enteros distintos, en orden inverso
    """
    return list(range(n))