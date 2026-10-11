"""Módulo para calcular el promedio de una lista de números aplicando PEP 8."""


def calcular_promedio(lista_numeros: list[int]) -> float:
    """Calcula el promedio de una lista de números enteros.

    Args:
        lista_numeros: Una lista de números enteros para promediar.

    Returns:
        El valor flotante correspondiente al promedio de los elementos.
    """
    suma_total = 0
    for numero in lista_numeros:
        suma_total = suma_total + numero
    return suma_total / len(lista_numeros)


def main() -> None:
    """ Punto de entrada principal del script."""
    numeros = [1, 2, 3, 4, 5]
    resultado = calcular_promedio(numeros)
    print(f"El promedio es: {resultado}")


if __name__ == "__main__":
    main()