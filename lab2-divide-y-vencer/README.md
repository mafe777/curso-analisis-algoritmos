# Laboratorio 02: Algoritmos de Dividir y Vencerás (Subarreglo Máximo)

**Autor:** Maria Fernanda Muñoz Jaramillo  
**Curso:** Análisis y Diseño de Algoritmos  

---

## Resumen y Reproducción del Experimento

Este laboratorio se centra en la implementación y comparación de dos métodos distintos para enfrentar el reto del Subarreglo Máximo (definir el subarreglo contiguo en una secuencia de números que tenga la suma más grande):
1. **Fuerza bruta:** al revisar todas las combinaciones posibles mediante bucles anidados.
2. **Dividir y conquistar:** al dividir el problema en mitades de forma recursiva y combinar los resultados.

### Pasos para reproducir
Los siguientes comandos deben ejecutarse **desde la raíz del repositorio** (`curso-analisis-algoritmos/`) con el entorno virtual activo:

1. Activar el entorno virtual (PowerShell):
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
2. Para ejecutar el script de pruebas unitarias y validación con enteros aleatorios (-100 a 100):
   ```powershell
   python lab2-divide-y-vencer/pruebas.py
   ```
3. Para ejecutar el script que calcula los tiempos y genera la gráfica de rendimiento:
   ```powershell
   python lab2-divide-y-vencer/medicion.py
   ```

---

## Parte 1 — Descripción de verificación y pruebas

**Archivos asociados:** [subarreglo.py](subarreglo.py) | [pruebas.py](pruebas.py)

En esta parte se elaboraron los algoritmos principales siguiendo las normas de estilo PEP 8, añadiendo type hints y docstrings detallados en estilo Google. El archivo `pruebas.py` se encarga de garantizar el correcto funcionamiento a través de:
1. Combinación del caso base relacionado con la serie de prueba de 8 días que se nos enseñó en la guía.
2. La evaluación de situaciones límite, como listas que contienen un solo elemento, secuencias compuestas solo por números negativos y conjuntos variados.
3. La validación rigurosa con un mínimo de 20 iteraciones sobre listas de diferentes tamaños (usando enteros aleatorios con `random.randint(-100, 100)`), comparando los resultados de los dos algoritmos para verificar que arrojan exactamente la misma suma máxima.

---

## Parte 2 — Rendimiento

**Archivo asociado:** [medicion.py](medicion.py)

Para analizar el desempeño real, se registraron los tiempos de ejecución usando la función `time.perf_counter()`. Se evaluaron tamaños de entrada $n$ de 50, 100, 500, 1000, 2000 y 4000 elementos, además se estableció una semilla con `random.seed(42)` para garantizar que ambos métodos procesaran exactamente la misma secuencia de datos en cada ejecución.

**Gráfica comparativa de tiempos:**
![Gráfica de Rendimiento](graficas/rendimiento_dv.png)

---

## Parte 3 — Respuestas del análisis

### 1. Recurrencia y Teorema Maestro
- **Planteamiento:** El algoritmo divide el arreglo en 2 subproblemas de tamaño $n/2$ ($2T(n/2)$) y un caso cruzado evaluado por la función auxiliar de combinación, planteando la ecuación de recurrencia $T(n) = 2T(n/2) + \Theta(n)$, con un caso base $T(1) = \Theta(1)$.
- **Origen de los términos:** El factor $2T(n/2)$ proviene de las dos llamadas recursivas independientes sobre las mitades del arreglo. El término $\Theta(n)$ representa el trabajo lineal invertido por la función de cruce al recorrer los elementos hacia la izquierda y derecha desde el punto medio.
- **Solución Teorema Maestro:** Aplicando el **Caso 2** del Teorema Maestro ($a=2, b=2$, de modo que $n^{\log_b a} = n^{\log_2 2} = \Theta(n)$, y el costo de combinación es $f(n) = \Theta(n)$), se concluye que la complejidad estricta de tiempo es $\Theta(n \log n)$. Por su parte, la **Fuerza Bruta** tiene una complejidad de $\Theta(n^2)$ ya que emplea dos bucles anidados para revisar todas las combinaciones posibles de forma proporcional a $n(n-1)/2$.

### 2. Lo medido contra lo esperado
- **Comportamiento de las curvas:** La curva que presenta la fuerza bruta indica un aumento rápido a medida que $n$ incrementa, volviéndose muy costosa. En cambio, la curva del enfoque de dividir y vencer es mucho más estable y eficiente.
- **Duplicación de $n$:** Si tomamos los tamaños de $n=500$ y $n=1000$, donde $n$ se duplica, el tiempo de fuerza bruta se eleva de $0.0058$ s a alrededor de $0.0354$ s, incrementándose por un factor cercano a $6.1$ (alineado con el crecimiento cuadrático $\Theta(n^2)$ y la sobrecarga del intérprete). Por el contrario, el tiempo para dividir y vencerás va de aprox. $0.0019$ s a $0.0041$ s, duplicándose de forma cercana a un factor de $2.15$, lo cual valida empíricamente el comportamiento teórico de $\Theta(n \log n)$.

### 3. Tamaños pequeños y umbral ($n=500$)
En las mediciones se puede notar que para valores muy bajos los tiempos de los dos algoritmos son muy similares e incluso la fuerza bruta puede parecer competitiva. Esto sucede porque la carga de gestionar las llamadas recursivas en Python supera las ventajas de descomponer el problema cuando la cantidad de datos es pequeña. A partir de **$n = 500$** se vuelve notable y definitiva la ventaja del enfoque de dividir y vencerás, tal como lo reflejan los valores medidos:

| Tamaño ($n$) | Tiempo Fuerza Bruta (s) | Tiempo Divide y Vencerás (s) |
| :----------- | :--------------         | :-------------------------   |
| 50           | 0.00012                 | 0.00015                      |
| 100          | 0.00045                 | 0.00032                      |
| 500          | 0.00580                 | 0.00190                      |
| 1000         | 0.03540                 | 0.00410                      |

### 4. Cuándo conviene dividir
No conviene aplicar esta técnica para encontrar el máximo simple de un arreglo, ya que recorrerlo linealmente cuesta $\Theta(n)$ y aplicar Divide y Vencerás con $T(n) = 2T(n/2) + \Theta(1)$ solo añadiría costos ocultos de llamadas recursivas innecesarias para obtener un resultado que ya se logra en un solo recorrido. Dividir y vencerás solo es beneficioso cuando la combinación o intersección de los subproblemas aporta información estructural crítica que optimiza la solución global (como ocurre en el subarreglo máximo cruzado).

### 5. Concepto para la gerente (Escalamiento a 1.000.000 de registros)
- **Recomendación:** Aplicar el algoritmo de Divide y Vencerás.
- **Estimación cuantitativa:** Procesar $1.000.000$ de registros utilizando un método de fuerza bruta $\Theta(n^2)$ requeriría aproximadamente $(10^6)^2 = 10^{12}$ operaciones, lo que se traduciría teóricamente en **muchas horas de cálculo continuo**, haciéndolo completamente inviable para la operación. En contraste, resolverlo con Divide y Vencerás $\Theta(n \log n)$ requiere del orden de $10^6 \times \log_2(10^6) \approx 2 \times 10^7$ operaciones, permitiendo procesar el problema en **una fracción muy corta de segundo** (estimado en menos de $0.08$ segundos), garantizando la eficiencia asintótica que el sistema empresarial requiere.