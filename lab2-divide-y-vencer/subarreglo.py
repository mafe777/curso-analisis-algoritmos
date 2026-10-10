"""Subarreglo máximo: implementación por fuerza bruta y divide y vencerás."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de días (i, j).

    Args:
        valores: variación diaria de caja, una por día. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los índices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor_inicio = 0
    mejor_fin = 0
    max_suma = valores[0]

    for i in range(n):
        suma_actual = 0.0
        for j in range(i, n):
            suma_actual += valores[j]
            if suma_actual > max_suma:
                max_suma = suma_actual
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, max_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variación diaria de caja.
        inicio: índice inicial del rango considerado (inclusive).
        medio: índice del último elemento de la mitad izquierda.
        fin: índice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    suma_izq = float("-inf")
    suma_acumulada = 0.0
    mejor_izq = medio

    for i in range(medio, inicio - 1, -1):
        suma_acumulada += valores[i]
        if suma_acumulada > suma_izq:
            suma_izq = suma_acumulada
            mejor_izq = i

    suma_der = float("-inf")
    suma_acumulada = 0.0
    mejor_der = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_acumulada += valores[j]
        if suma_acumulada > suma_der:
            suma_der = suma_acumulada
            mejor_der = j

    return mejor_izq, mejor_der, suma_izq + suma_der


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y vencerás.

    Args:
        valores: variación diaria de caja.
        inicio: índice inicial del rango a considerar (inclusive).
        fin: índice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    i_izq, f_izq, suma_izq = subarreglo_maximo(valores, inicio, medio)
    i_der, f_der, suma_der = subarreglo_maximo(valores, medio + 1, fin)
    i_cruz, f_cruz, suma_cruz = suma_cruzada(valores, inicio, medio, fin)

    if suma_izq >= suma_der and suma_izq >= suma_cruz:
        return i_izq, f_izq, suma_izq
    elif suma_der >= suma_izq and suma_der >= suma_cruz:
        return i_der, f_der, suma_der
    else:
        return i_cruz, f_cruz, suma_cruz