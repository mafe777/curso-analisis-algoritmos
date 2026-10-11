"""algoritmos de ordenamiento instrumentados para el Laboratorio 1"""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion

    No modifica la lista recibida: trabaja sobre una copia

    Args:
        datos: lista de indices de riesgo a ordenar

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso
    """
    lista = list(datos)
    comparaciones = 0

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if lista[j] < actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break

        lista[j + 1] = actual

    return lista, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla

    No modifica la lista recibida: trabaja sobre una copia

    Args:
        datos: lista de indices de riesgo a ordenar

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso
    """
    lista = list(datos)
    
    def _merge_sort(sub_lista: list[int]) -> tuple[list[int], int]:
        if len(sub_lista) <= 1:
            return sub_lista, 0

        medio = len(sub_lista) // 2
        izq, comps_izq = _merge_sort(sub_lista[:medio])
        der, comps_der = _merge_sort(sub_lista[medio:])

        mezclada, comps_mezcla = _mezclar(izq, der)
        total_comps = comps_izq + comps_der + comps_mezcla
        return mezclada, total_comps

    def _mezclar(izq: list[int], der: list[int]) -> tuple[list[int], int]:
        resultado = []
        i = j = 0
        comparaciones = 0

        # Ordenamos de mayor a menor riesgo para Tamiza
        while i < len(izq) and j < len(der):
            comparaciones += 1
            if izq[i] >= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado, comparaciones

    lista_ordenada, total_comparaciones = _merge_sort(lista)
    return lista_ordenada, total_comparaciones