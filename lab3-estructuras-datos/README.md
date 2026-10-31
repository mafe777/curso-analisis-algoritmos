# Laboratorio 3: Estructuras de datos (Rutas del Caribe)

**Autor:** Maria Fernanda Muñoz Jaramillo
**Curso:** Análisis y Diseño de Algoritmos  

---

## Instrucciones para reproducir el experimento

1. **Activar el entorno virtual** en la raiz del repositorio (`curso-analisis-algoritmos`):
   - En Windows (PowerShell):
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
2. **Ejecutar las pruebas unitarias:**
   ```powershell
   python lab3-estructuras-datos/pruebas.py

3. **Ejecutar los experimentos y generar las gráficas:**
   ```powershell
   python lab3-estructuras-datos/medicion.py

  ## Implementación y verificación
  La validación se llevó a cabo a través de pruebas unitarias con afirmaciones que abarcaban: 
  - búsquedas tanto exitosas como fallidas en la lista enlazada y en la tabla hash.
  - Se provocó una colisión con m = 7 utilizando las claves 10, 24 y 17 (todas ellas ubicadas en la posición 3), verificando que la longitud de la lista en esa posición es exactamente 3.
  - Se validó de manera correcta el cálculo del factor de carga (alpha = 3/7).
  - Se realizaron veinte colecciones aleatorias comparando los resultados de búsqueda en ambas estructuras para garantizar una consistencia total.

  ##Medición y experimentación
Para realizar las mediciones, se utilizo time.perf_counter() al evaluar 200 búsquedas de guías que no existían, utilizando una semilla constante (random.seed(42) y semilla=7), lo que garantizaba que las condiciones fueran iguales para ambas configuraciones. En el experimento A, se aplicaron seis tamaños de entrada ($n \in \{100, 500, 1000, 5000, 20000, 50000\}$) con $m \approx n/2$. En el experimento B, se estableció $n = 20000$ y se modificó $m$ para conseguir factores de carga de $0.25, 1.0, 4.0$ y $10.0$.

Gráfica 1: Lista enlazada frente a Tabla Hash
Gráfica 2: Efecto del factor de carga ($\alpha$)

— Análisis-
1. costo teorico:La lista enlazada examina cada nodo uno por uno en el escenario más desfavorable, lo que cuesta $\Theta(n)$. La tabla hash accede directamente al espacio correspondiente y luego revisa una lista pequeña, con un costo promedio de $\Theta(1 + \alpha)$ suponiendo que hay un hashing uniforme (si ocurre una colisión, el costo aumenta a $\Theta(n)$).
2. lo medido vs lo esperado:El primer gráfico verifica el aumento lineal de la lista ($\Theta(n)$) en comparación con la línea horizontal de la tabla hash ($\Theta(1)$). El segundo gráfico confirma que el tiempo aumenta de manera gradual al aumentar el factor de carga $\alpha$.
3. colisiones:Son imposibles de evitar debido a la regla del palomar. El encadenamiento las soluciona mediante listas internas (que son adaptables, pero ocupan más memoria) y el direccionamiento abierto que busca espacios vacíos. Por ejemplo: con $m = 7$, las claves 10, 24 y 17 colisionan en la posición 3 ($x \pmod 7 = 3$).