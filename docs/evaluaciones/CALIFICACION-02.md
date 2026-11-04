# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Maria Fernanda Muñoz Jaramillo · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `3a0792e`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 11 / 20 |
| Calidad de la explicación teórica | 11 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 15 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **69 / 100** |
| **Nota (0–5)** | **3.45** |

## 1. Corrección conceptual (11 / 20)
**Lo que hizo bien:**
- En la pregunta 4 explica que dividir no conviene para hallar el máximo de un arreglo, porque recorrerlo una vez ya cuesta `Θ(n)` y dividir solo agrega trabajo extra.
- En la pregunta 5 recomienda divide y vencerás y dice que la fuerza bruta sería poco práctica con 1.000.000 de registros.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 no explica cuánto cuesta combinar las dos mitades ni a qué resultado lleva la recurrencia del máximo.
  → *Cómo corregirlo:* escriba la recurrencia del máximo dividido, diga cuánto cuesta unir las dos respuestas y compare el resultado con recorrerlo una vez.
- En la pregunta 5 no da una estimación de tiempo para 1.000.000 de registros ("muchas horas" y "una fracción muy corta de segundo" no son cifras) y no aclara que es una estimación.
  → *Cómo corregirlo:* parta de un tiempo que usted midió, use la forma de cada curva (`n²` y `n log n`) para escalarlo a 1.000.000 y escriba que es una estimación.
- En la pregunta 3 dice que la ventaja se nota "a partir de n=500", pero no se apoya en valores de sus mediciones en los tamaños pequeños.
  → *Cómo corregirlo:* agregue una tabla con los tiempos medidos en cada tamaño e indique en cuál el divide y vencerás pasa a ganar.

## 2. Calidad de la explicación teórica (11 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, identifica `a=2`, `b=2` y llega a `Θ(n log n)` con el caso 2 del método maestro.
- Justifica que la fuerza bruta es `Θ(n²)` por sus dos ciclos anidados.

**Lo que puede mejorar (y cómo corregirlo):**
- No explica de dónde sale cada término: por qué hay dos subproblemas, por qué de tamaño n/2 y por qué el caso cruzado cuesta `Θ(n)`.
  → *Cómo corregirlo:* escriba una frase por término, mirando lo que hace su `suma_cruzada`.
- No verifica la condición del caso 2 del método maestro.
  → *Cómo corregirlo:* calcule `n^(log_b a)` con sus valores y compárelo con `f(n)` para mostrar por qué aplica ese caso.
- La recurrencia está mezclada con texto y quedó confusa.
  → *Cómo corregirlo:* escriba la recurrencia completa una sola vez, incluyendo el caso base.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones están bien: devuelven la suma correcta en la serie de ocho días, un elemento, todo negativo, todo positivo y un caso cruzado.
- `subarreglo_maximo` resuelve los tres casos, no llama a la fuerza bruta y no modifica la lista.
- `pruebas.py` cubre todos los casos pedidos y compara 20 listas aleatorias.
- Tiene docstrings con `Args` y `Returns`, type hints y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- Las pruebas aleatorias y la medición usan números decimales (`random.uniform`), pero se pedían enteros entre -100 y 100.
  → *Cómo corregirlo:* use `random.randint(-100, 100)`.
- En `medicion.py` las funciones no tienen la estructura de comentarios alineada con el código (un comentario queda sin sangría dentro de la función).
  → *Cómo corregirlo:* indente ese comentario dentro de `ejecutar_experimento`.

## 4. Calidad del análisis de las gráficas (15 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, y se ve en el informe.
- Mide 6 tamaños, con dos menores de 100 y uno de 4000, con semilla fija, y verifica que ambas funciones den la misma suma.
- Los valores del informe para la fuerza bruta (unos 0.006 s en n=500 y 0.036 s en n=1000) coinciden con la gráfica.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 2 el factor de la fuerza bruta (cerca de 6) se da por bueno para `Θ(n²)`, que predice un factor cercano a 4, y se explica solo con "sobrecarga de llamadas", que no aplica a la fuerza bruta.
  → *Cómo corregirlo:* compare su factor con el que predice `n²` al duplicar y diga cuánto se desvía.
- Para divide y vencerás dice que "se duplica de forma lineal", sin calcular el factor y sin contrastarlo con `n log n`.
  → *Cómo corregirlo:* calcule tiempo(1000)/tiempo(500) y compárelo con el factor que predice `n log n` al duplicar `n`.
- Con una sola medición por tamaño y sin tabla, los tamaños pequeños no se pueden leer en la gráfica.
  → *Cómo corregirlo:* repita cada medición unas tres veces, use el promedio o la mediana, y agregue una tabla con los valores.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` y sus archivos siguen la estructura pedida.
- El informe sigue el orden pedido, trae su nombre, enlaza el código en cada parte y la gráfica se ve.
- Tiene tres commits descriptivos del laboratorio.

**Lo que puede mejorar (y cómo corregirlo):**
- Las instrucciones de reproducción no dicen que los comandos se ejecutan desde la raíz del repositorio; `medicion.py` guarda la gráfica con una ruta que solo funciona así.
  → *Cómo corregirlo:* aclare desde qué carpeta se ejecuta cada comando.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y las dos funciones dan la misma suma. La medición está pensada para generar la gráfica ejecutándola desde la raíz del repositorio.
