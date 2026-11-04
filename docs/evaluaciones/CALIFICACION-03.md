# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Maria Fernanda Muñoz Jaramillo · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `3a0792e`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 8 / 20 |
| Calidad de la explicación teórica | 12 / 20 |
| Corrección de la implementación | 17 / 25 |
| Calidad del análisis de las gráficas | 10 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **53 / 100** |
| **Nota (0–5)** | **2.65** |

## 1. Corrección conceptual (8 / 20)
**Lo que hizo bien:**
- Explica que las colisiones son inevitables (principio del palomar) y usa el ejemplo de las guías 10, 24 y 17 con m = 7.
- Dice con claridad que la tabla hash no sirve para consultas por rango.
- Propone combinar tabla hash y árbol equilibrado.

**Lo que puede mejorar (y cómo corregirlo):**
- La explicación de colisiones es muy corta: no compara las ventajas y costos del encadenamiento y del direccionamiento abierto, y no muestra cómo queda la casilla 3 con el ejemplo.
  → *Cómo corregirlo:* para cada método escriba una ventaja y un costo, y dibuje o describa qué ocurre con 10, 24 y 17 en cada uno.
- En la pregunta 4 no estima la altura ni las comparaciones del árbol degenerado con 400.000 guías, ni las del árbol equilibrado; solo dice "línea recta" y "log₂ n".
  → *Cómo corregirlo:* piense cuántos niveles tiene un árbol que es una cadena de 400.000 nodos y cuántos tiene uno equilibrado, y calcule las comparaciones de una búsqueda en cada caso.
- En la pregunta 5 no da la estimación pedida para 5.000.000 de envíos (ni para la lista ni para la tabla); solo dice "microsegundos".
  → *Cómo corregirlo:* parta de sus propias mediciones, razone cómo crece cada curva, calcule el tiempo de cada estructura y diga explícitamente que es una estimación.

## 2. Calidad de la explicación teórica (12 / 20)
**Lo que hizo bien:**
- Nombra el Θ(n) de la lista y el Θ(1 + α) de la tabla, el supuesto de hash uniforme y que si todo cae en una casilla el costo sube a Θ(n).

**Lo que puede mejorar (y cómo corregirlo):**
- Solo afirma los resultados; no explica de dónde sale cada costo (por qué se recorren n nodos, por qué el 1 y el α en la tabla) ni qué significa el supuesto de hash uniforme.
  → *Cómo corregirlo:* explique, con sus palabras, cuántos nodos revisa una búsqueda que falla en la lista, y cuántos tiene en promedio la lista de una casilla cuando las guías se reparten por igual.
- No dice qué pasaría con la tabla en el caso extremo (en qué se convierte).
  → *Cómo corregirlo:* compare esa tabla con otra estructura que ya conoce.

## 3. Corrección de la implementación (17 / 25)
**Lo que hizo bien:**
- Ambas estructuras funcionan: la búsqueda exitosa e infructuosa, la colisión con m = 7, el factor de carga 3/7 y las 20 colecciones aleatorias pasan.
- La tabla reutiliza la lista, sin `dict`, `set` ni `hash()`, y la búsqueda es con `while`.
- Tiene type hints y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- Los docstrings no tienen las secciones `Args` y `Returns`, y `Nodo.__init__`, `ListaEnlazada.__init__` y `TablaHash.__init__` no tienen docstring.
  → *Cómo corregirlo:* siga el formato Google que trae el enunciado: descripción, `Args:` con cada parámetro y `Returns:` con lo que devuelve.
- Los docstrings de `medicion.py` tampoco tienen `Args` y `Returns`.
  → *Cómo corregirlo:* complételos igual que en `estructuras.py`.

## 4. Calidad del análisis de las gráficas (10 / 25)
**Lo que hizo bien:**
- Las dos gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de n con ambas curvas en los mismos ejes y la segunda cuatro valores de α.
- Cronometra solo las búsquedas con `time.perf_counter()` y usa semilla fija.

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 2 no calcula ningún factor de crecimiento ni cita valores de las gráficas; solo dice que la lista "sube" y la tabla es "horizontal".
  → *Cómo corregirlo:* tome dos valores consecutivos de n, lea el tiempo de cada estructura en la primera gráfica, calcule cuántas veces creció cada uno y compárelo con lo que predice Θ(n) y Θ(1).
- En la segunda gráfica el tiempo baja de α = 0,25 a α = 1 y el informe lo ignora al decir que "aumenta gradualmente".
  → *Cómo corregirlo:* describa lo que realmente ve en cada punto y explique la irregularidad (por ejemplo el ruido de medir tiempos muy pequeños) frente a Θ(1 + α).
- Dentro del experimento no verifica que lista y tabla den el mismo estado para una muestra de guías existentes.
  → *Cómo corregirlo:* antes de medir, busque unas cuantas guías existentes en ambas estructuras y compárelas con `assert`.
- Usa m = n/2 sin ser primo, y el informe no lo dice con claridad.
  → *Cómo corregirlo:* elija un primo cercano a n/2 y escriba en el informe qué m usó para cada n.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Usó la carpeta `lab3-estructuras-datos/` con los archivos pedidos y las gráficas incrustadas con ruta relativa que se resuelve.
- El informe sigue el orden pedido, trae su nombre y tiene 4 commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- No enlaza el código: faltan los enlaces a `estructuras.py` y `pruebas.py` en la Parte 1 y a `medicion.py` en la Parte 2.
  → *Cómo corregirlo:* al inicio de cada parte agregue enlaces Markdown como `[estructuras.py](estructuras.py)`.
- Las instrucciones de reproducción solo cubren Windows y los comandos asumen ejecutar desde la raíz del repositorio sin decirlo.
  → *Cómo corregirlo:* indique también la activación en macOS/Linux y desde qué carpeta ejecutar.
- El archivo `requirements.txt` quedó guardado en un formato que muchos programas no leen bien (codificación UTF-16).
  → *Cómo corregirlo:* vuelva a generarlo en UTF-8.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre y genera las dos gráficas sin errores.
