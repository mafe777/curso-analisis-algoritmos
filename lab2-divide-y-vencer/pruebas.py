"""Script de pruebas para los algoritmos de subarreglo máximo."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

# Serie de ocho dias de la situacion problema
serie_ejemplo = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie_ejemplo)[2] == 17
assert subarreglo_maximo(serie_ejemplo, 0, len(serie_ejemplo) - 1)[2] == 17

#  Serie de un solo elemento
serie_un_elemento = [42]
assert subarreglo_fuerza_bruta(serie_un_elemento)[2] == 42
assert subarreglo_maximo(serie_un_elemento, 0, 0)[2] == 42

# Serie con todos los valores negativos
serie_negativa = [-5, -2, -9, -1]
assert subarreglo_fuerza_bruta(serie_negativa)[2] == -1
assert subarreglo_maximo(serie_negativa, 0, len(serie_negativa) - 1)[2] == -1

#  Serie con todos los valores positivos
serie_positiva = [2, 4, 6, 8]
assert subarreglo_fuerza_bruta(serie_positiva)[2] == 20
assert subarreglo_maximo(serie_positiva, 0, len(serie_positiva) - 1)[2] == 20

# Caso donde el mejor tramo cruza el punto medio 
serie_cruce = [1, -3, 5, 5, -3, 1]  # [5, 5] cruza el centro
assert subarreglo_fuerza_bruta(serie_cruce)[2] == 10
assert subarreglo_maximo(serie_cruce, 0, len(serie_cruce) - 1)[2] == 10

#  Al menos veinte listas aleatorias comparando las soluciones
random.seed(42)
for k in range(20):
    tam = random.randint(5, 50)
    lista_aleatoria = [random.uniform(-50, 50) for _ in range(tam)]
    res_fb = subarreglo_fuerza_bruta(lista_aleatoria)
    res_dyv = subarreglo_maximo(lista_aleatoria, 0, len(lista_aleatoria) - 1)
  
    assert abs(res_fb[2] - res_dyv[2]) < 1e-5
print("¡Todas las pruebas pasaron exitosamente sin errores!")
if __name__ == "__main__":
    pass