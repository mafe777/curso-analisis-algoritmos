# Laboratorio 03 — Estructuras de datos (Rutas del Caribe)

**Autor:** Maria Fernanda Muñoz Jaramillo  
**Curso:** Análisis de Algoritmos  

---

## Instrucciones de Reproducción

Los siguientes comandos deben ejecutarse **desde la raíz del repositorio** (`curso-analisis-algoritmos/`) con el entorno virtual activo:

1. **Activar el entorno virtual (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
*(Nota para macOS/Linux: `source .venv/bin/activate`)*

2. **Ejecutar las pruebas unitarias y de verificación:**
   ```powershell
   python lab3-estructuras-datos/pruebas.py
   ```

3. **Ejecutar los experimentos de medición y generar las gráficas:**
   ```powershell
   python lab3-estructuras-datos/medicion.py
   ```

---

## Parte 1 — Implementación y Verificación

**Enlaces al código:**  
* [estructuras.py](estructuras.py) — Clases Nodo, ListaEnlazada y TablaHash.  
* [pruebas.py](pruebas.py) — Script de validación con `assert`.

### Verificación realizada:
Se comprobó la correctitud de las estructuras mediante el script `pruebas.py`, cubriendo:
1. **Búsquedas exitosas e infructuosas** para validar la recuperación exacta de estados.
2. **Colisión forzada:** Configurando $m = 7$ y las guías 10, 24 y 17 (cuyos módulos respectivos `10 % 7`, `24 % 7` y `17 % 7` arrojan todas residuo 3), demostrando que las tres se insertan correctamente en la misma casilla, su lista interna alcanza longitud 3 y se recuperan sin alterar sus datos.
3. **Factor de carga:** Comprobando que `factor_carga()` retorna exactamente $3 / 7$ tras las tres inserciones mencionadas.
4. **Colecciones aleatorias:** Evaluando 20 colecciones dinámicas de tamaños variados, contrastando que la lista enlazada y la tabla hash devuelven idénticos resultados tanto para elementos existentes como inexistentes.

---

## Parte 2 — Medición y Rendimiento

**Enlace al código:**  
* [medicion.py](medicion.py) — Script de cronometraje y exportación gráfica.

### Notas del experimento:
* Se evaluaron seis tamaños de entrada para $n$ ($100, 500, 1000, 5000, 10000, 20000$). Para cada $n$, se seleccionó un número primo $m$ cercano a $n / 2$ para garantizar un factor de carga $\alpha \approx 2$.
* Se cronometraron estrictamente $200$ búsquedas de guías inexistentes utilizando `time.perf_counter()`, repitiendo el proceso y promediando los resultados para mitigar el ruido del sistema operativo.
* Se validó mediante `assert` dentro del experimento que ambas estructuras arrojaran el mismo resultado antes de iniciar el cronometraje.

**Gráfica 1: Lista Enlazada frente a Tabla Hash ($n$)**  
![Lista vs Tabla](graficas/lista_vs_tabla.png)

**Gráfica 2: Efecto del Factor de Carga ($\alpha$) con $n = 20.000$**  
![Tiempo vs Alfa](graficas/tiempo_vs_alfa.png)

---

## Parte 3 — Análisis en el README

### 1. Costo teórico
* **Lista enlazada:** Buscar una guía inexistente exige recorrer toda la estructura desde la cabeza hasta el último nodo, visitando $n$ nodos. Por lo tanto, el tiempo de búsqueda crece de forma lineal, es decir, $\Theta(n)$.
* **Tabla hash con encadenamiento:** Buscar una clave requiere calcular la posición con la función hash $\Theta(1)$ y luego recorrer la lista enlazada alojada en dicha casilla. Bajo el **supuesto de hash uniforme simple** (el cual establece que cualquier clave tiene la misma probabilidad de ser asignada a cualquiera de las $m$ casillas, de manera independiente de las demás), el número esperado de elementos por casilla es el factor de carga $\alpha = n / m$. Así, el costo esperado de la búsqueda es $\Theta(1 + \alpha)$.
* **Caso extremo:** Si todas las guías cayeran en la misma casilla (por una función hash defectuosa o un ataque deliberado), la tabla hash se degrada estructuralmente y se convierte en una **única lista enlazada de tamaño $n$**, elevando el costo de búsqueda a $\Theta(n)$.

### 2. Lo medido contra lo esperado
* **De la primera gráfica (Lista vs. Tabla):** Tomando los valores consecutivos $n = 10.000$ y $n = 20.000$ en la lista enlazada, el tiempo pasa aproximadamente de $0.00045$ s a $0.00090$ s, duplicándose por un factor cercano a $2.0$, lo cual coincide perfectamente con el comportamiento teórico $\Theta(n)$. En contraste, la curva de la tabla hash permanece horizontal y cercana al eje horizontal con un crecimiento despreciable, reflejando el comportamiento constante $\Theta(1 + \alpha)$.
* **De la segunda gráfica (Efecto de $\alpha$):** Se observa que al incrementar el factor de carga $\alpha$ (al reducir el número de casillas $m$ para un $n$ fijo de $20.000$), el tiempo medio de búsqueda aumenta de manera proporcional al tamaño de las listas internas de cada casilla, lo cual es plenamente coherente con la expresión teórica $\Theta(1 + \alpha)$.

### 3. Explique las colisiones
* **Definición y causa:** Una colisión ocurre cuando dos claves distintas $k_1 \neq k_2$ producen el mismo valor al ser procesadas por la función hash ($h(k_1) = h(k_2)$). Esto es inevitable debido al **Principio del Palomar**: el dominio de posibles números de guía de diez dígitos es inmensamente mayor que el número de casillas $m$ disponibles en la tabla.
* **Manejo de colisiones:**
  * **Encadenamiento:** Cada casilla almacena una lista enlazada. Si ocurre una colisión, el nuevo elemento se simplemente añade a dicha lista.
    * *Ventaja:* Simple de implementar, tolera factores de carga $\alpha > 1$ sin fallar.
    * *Costo:* Requiere memoria adicional dinamica para los punteros de los nodos.
  * **Direccionamiento Abierto:** Todos los elementos se almacenan directamente en el arreglo principal; si hay colisión, se busca una casilla alternativa vacía mediante sondeo (lineal, cuadrático o doble hash).
    * *Ventaja:* Uso eficiente de memoria al evitar punteros externos.
    * *Costo:* Es susceptible a la congestión de casillas (*clustering*) y el factor de carga debe mantenerse estrictamente menor que 1 ($\alpha < 1$).
* **Ejemplo con $m = 7$ y guías 10, 24 y 17:** Al aplicar $h(k) = k \pmod 7$, se tiene que $10 \pmod 7 = 3$, $24 \pmod 7 = 3$ y $17 \pmod 7 = 3$. En el **encadenamiento**, la casilla 3 contendrá una lista enlazada con tres nodos conectados en secuencia (`Nodo(17) -> Nodo(24) -> Nodo(10)`). En el **direccionamiento abierto** (por ejemplo, con sondeo lineal), la guía 10 ocupa la casilla 3; al intentar insertar la guía 24, se detecta ocupación y se desplaza a la siguiente casilla libre (casilla 4), y la guía 17 se desplaza a la casilla 5.

### 4. Tabla hash o árbol de búsqueda
* **Para el monitoreo por rango ("guías entre X y Y"):** La tabla hash **no sirve**, ya que organiza los datos en función de los residuos de la función hash y no mantiene ningún orden secuencial o numérico; consultar un rango exigiría inspeccionar toda la tabla (fuerza bruta).
* **Alternativa con Árbol de Búsqueda Binario (ABB):** Un árbol equilibrado (como un AVL o Rojinegro) mantiene las claves ordenadas, permitiendo localizar el límite inferior del rango en tiempo $O(\log n)$ y recorrer los nodos subsecuentes de manera eficiente.
* **Escenario de inserción ordenada (400.000 guías):** Si las 400.000 guías llegaran ya ordenadas e se insertaran secuencialmente en un ABB estándar sin balanceo, el árbol se **degeneraría** convirtiéndose en una cadena lineal.
  * *Altura resultante:* $h = 400.000$ niveles.
  * *Comparaciones en búsqueda:* En el peor de los casos requeriría hasta $400.000$ comparaciones ($\Theta(n)$).
  * *Comparación con árbol equilibrado:* Un árbol equilibrado con $n = 400.000$ tendría una altura de $h = \log_2(400.000) \approx 19$ niveles, requiriendo como máximo unas $19$ comparaciones para una búsqueda ($\Theta(\log n)$).

### 5. Concepto para la jefa de operaciones
* **Recomendación arquitectónica:** Se recomienda implementar una **arquitectura híbrida o combinar estructuras**: mantener una **Tabla Hash** exclusiva para las consultas puntuales del call center (garantizando velocidad ultra rápida $\Theta(1)$ para verificar estados de forma aislada), y respaldarla con un **Árbol de Búsqueda Binario Equilibrado** (o una estructura auxiliar ordenada) para atender las solicitudes diarias de monitoreo por rango de los supervisores.
* **Estimación cuantitativa para 5.000.000 de envíos:** *(Nota: Esto corresponde a una estimación matemática proyectada a partir del comportamiento asintótico observado).*
  * Con base en las mediciones empíricas para $n = 20.000$ donde la búsqueda infructuosa en la tabla hash tomó en promedio $\approx 0.0000012$ segundos ($\sim 1.2$ microsegundos) con un factor de carga constante $\alpha \approx 2$, podemos proyectar que, al escalar a $5.000.000$ de envíos manteniendo el mismo factor de carga (ampliando $m$ proporcionalmente), el tiempo de búsqueda en la **Tabla Hash** seguirá siendo constante, estimándose en aproximadamente **$1.5$ a $2.0$ microsegundos**.
  * En contraste, para la **Lista Enlazada**, dado su crecimiento lineal $\Theta(n)$, si con $20.000$ elementos tardó $\approx 0.0009$ segundos, al multiplicar el volumen por un factor de $250$ ($5.000.000 / 20.000$), el tiempo de búsqueda se elevará linealmente a **aproximadamente $0.225$ segundos** ($225$ milisegundos) por cada consulta fallida, lo cual colapsaría el call center en horas pico.