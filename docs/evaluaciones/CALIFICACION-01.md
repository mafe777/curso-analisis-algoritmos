# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Maria Fernanda Muñoz Jaramillo · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `3a0792e`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 0 / 25 |
| Calidad de la explicación teórica | 0 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 3 / 20 |
| Documentación y organización del informe | 2 / 10 |
| **Total** | **22 / 100** |
| **Nota (0–5)** | **1.10** |

## 1. Corrección conceptual (0 / 25)
**Lo que puede mejorar (y cómo corregirlo):**
- El informe `README.md` quedó sin las Partes 1 y 2: el texto se corta en las instrucciones de reproducción, así que no hay respuestas sobre Tamiza.
  → *Cómo corregirlo:* agregue un encabezado por parte y responda cada pregunta con sus palabras, siguiendo los requisitos de cada parte de la guía (corrección vs. eficiencia, servidor más rápido, segundo ejemplo propio, energía, perjuicios y quién asume el costo, obligación sobre el orden de la lista).

## 2. Calidad de la explicación teórica (0 / 25)
**Lo que puede mejorar (y cómo corregirlo):**
- No están la explicación de los tres casos con su predicción (3.1), la recurrencia de merge sort resuelta paso a paso, el cálculo línea a línea de insertion sort ni la tabla de complejidades (4.1).
  → *Cómo corregirlo:* escriba estas secciones en el `README.md`; haga la predicción antes de comentar las gráficas, plantee la recurrencia explicando cada término y muestre el desarrollo completo con el método que elija.

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` trabajan sobre una copia, cuentan las comparaciones entre elementos y ordenan de mayor a menor de forma consistente.
- `merge_sort` tiene su propia mezcla recursiva y no se usa `sorted()` ni `sort()` en los algoritmos.
- Los tres generadores producen lotes del tamaño pedido y con semilla reproducible; el escenario C queda como el peor caso para el orden elegido.
- Los scripts corren sin errores y generan las gráficas.

**Lo que puede mejorar (y cómo corregirlo):**
- Las funciones internas `_merge_sort` y `_mezclar` no tienen *docstring* con `Args` y `Returns`, y algunos *docstrings* de otras funciones (por ejemplo en `parte3_casos.py` y `parte4_complejidad.py`) no traen `Args`/`Returns` completos.
  → *Cómo corregirlo:* agregue a cada función un *docstring* estilo Google con secciones `Args:` y `Returns:`.
- Falta una segunda línea en blanco entre `insertion_sort` y `merge_sort`.
  → *Cómo corregirlo:* deje dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (3 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y muestran las curvas en los mismos ejes.

**Lo que puede mejorar (y cómo corregirlo):**
- Las gráficas no están incrustadas en el `README.md` y no hay análisis: no se dice cuál escenario es el peor, el mejor y el promedio, ni cuál algoritmo conviene, ni hay concepto técnico (4.3) ni extrapolación a la ventana de cuatro horas.
  → *Cómo corregirlo:* incruste cada imagen con `![texto](graficas/parte3_tiempo.png)` y escriba, a partir de lo que ve en cada curva, sus conclusiones y la sección 4.3 pedida en la guía, declarando como estimación lo que extrapole.

## 5. Documentación y organización del informe (2 / 10)
**Lo que hizo bien:**
- Usó la carpeta correcta `lab1-fundamentos-complejidad-recurrencias/` con todos los archivos del entregable.
- El `README.md` trae su nombre y el inicio de las instrucciones de reproducción.

**Lo que puede mejorar (y cómo corregirlo):**
- Las instrucciones de reproducción están incompletas (se cortan tras activar el entorno) y el informe no está organizado por partes.
  → *Cómo corregirlo:* termine los pasos indicando el comando de cada parte (`python parte3_casos.py`, `python parte4_complejidad.py`).
- No hay enlaces al código (`algoritmos.py`, `datos.py`, `parte3_casos.py`, `parte4_complejidad.py`).
  → *Cómo corregirlo:* use enlaces como `[código de la Parte 3](parte3_casos.py)`.
- El laboratorio tiene un solo commit; se piden al menos cinco que muestren el avance.
  → *Cómo corregirlo:* haga commits pequeños y con mensajes descriptivos a medida que completa cada parte.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, los algoritmos ordenan correctamente y se generan las tres gráficas. Lo que falta es el informe escrito.
