# Proyecto 1 — Análisis de Complejidad Algorítmica

**Curso:** MM3032 - Lógica Matemática — Sección 20
**Universidad del Valle de Guatemala**

## Integrantes

| Nombre                              | Carnet |
|--------------------------------------|--------|
| Angel Gabriel Sanabria Morales       | 24725  |
| Javier Sebastián Alvarado Monzón     | 24546  |
| Vernel Josué Hernández Cáceres       | 24584  |
| Derek Friedhelm Coronado Chilin      | 24732  |
| Ronald Manuel Catún Chacón           | 19789  |

## Objetivo

Implementar, para cada orden de complejidad asignado, un algoritmo representativo en el
lenguaje de programación de preferencia de cada integrante, evidenciar numéricamente (con
capturas de pantalla) que la complejidad medida corresponde a la teórica, y resolver la
relación de recurrencia asociada mediante un método visto en clase.

## Estructura del repositorio

Cada carpeta contiene el algoritmo correspondiente a un orden de complejidad. El estado
indica si la sección ya fue documentada en este README.

| Carpeta               | Complejidad | Algoritmo sugerido           | Responsable | Estado        |
|------------------------|:-----------:|-------------------------------|-------------|:-------------:|
| `01_O_logn`            | O(log n)    | Búsqueda binaria               | Angel Gabriel Sanabria Morales | ✅ Completo |
| `02_O_n`                | O(n)        | Suma lineal / recorrido        | Por asignar | 🔲 Pendiente  |
| `03_O_nlogn`            | O(n log n)  | Mergesort                      | Por asignar | 🔲 Pendiente  |
| `04_O_n2`               | O(n²)       | Algoritmo cuadrático           | Por asignar | 🔲 Pendiente  |
| `05_O_n3`               | O(n³)       | Algoritmo cúbico               | Por asignar | 🔲 Pendiente  |
| `06_O_n10`              | O(n¹⁰)      | Algoritmo polinomial de grado 10 | Por asignar | 🔲 Pendiente |
| `07_O_nfactorial`       | O(n!)       | Generación de permutaciones    | Derek Friedhelm Coronado Chilin | ✅ Completo |
| `08_O_2n`               | O(2ⁿ)       | Suma de subconjuntos            | Angel Gabriel Sanabria Morales | ✅ Completo |

> Las capturas de pantalla de cada ejecución se guardan en `docs/<carpeta>/`, por ejemplo
> `docs/07_O_nfactorial/`.

---

## Cómo documentar tu sección (plantilla)

Cuando termines tu algoritmo, reemplaza el bloque `🔲 Pendiente` correspondiente en la tabla
de arriba por `✅ Completo`, agrega tu nombre en "Responsable", y copia esta plantilla al
final del README llenando cada parte. Las secciones 1, 7 y 8 ya están completas y sirven de
ejemplo.

```markdown
### N. O(<complejidad>) — <nombre del algoritmo>

**Carpeta:** `0N_O_<...>` · **Archivo:** `nombre_archivo.py` · **Responsable:** <nombre>

**Descripción del algoritmo**
(explica brevemente qué hace el algoritmo y por qué su complejidad es la indicada)

**Cómo ejecutarlo**
\`\`\`bash
cd 0N_O_<carpeta>
python nombre_archivo.py
\`\`\`

**Evidencia numérica de la complejidad**
(pega aquí la tabla/captura de pantalla de la ejecución, mostrando cómo crecen las
operaciones o el tiempo conforme crece n, y compáralo con la función de complejidad teórica)

![Ejecución](docs/0N_O_<carpeta>/ejecucion.png)

**Relación de recurrencia y resolución**
(plantea T(n) y resuélvela con un método visto en clase: sustitución, árbol de recursión,
teorema maestro, ecuación característica, etc. Muestra el desarrollo paso a paso.)
```

> Nota sobre la ruta de la imagen: este README está en la raíz del repositorio, así que la
> ruta correcta es `docs/0N_O_<carpeta>/ejecucion.png`, **sin** el `../` al inicio. Con `../`
> la ruta sale del repositorio y la imagen no carga en GitHub.

---

## Secciones completadas

### 1. O(log n) — Búsqueda binaria

**Carpeta:** `01_O_logn` · **Archivo:** `busqueda_binaria.py` · **Responsable:** Angel Gabriel Sanabria Morales

#### Descripción del algoritmo

El algoritmo busca un valor dentro de un arreglo **ordenado**. En cada llamada compara el
elemento que está a la mitad del rango contra el objetivo y, según el resultado, descarta la
mitad del arreglo y sigue buscando únicamente en la otra mitad.

Se implementó de forma **recursiva** y no iterativa a propósito, pues con un ciclo `while` no
existe una relación de recurrencia real que resolver; habría que inventarla. Escrito de forma
recursiva, la recurrencia `T(n) = T(n/2) + c` se lee directamente del código.

La complejidad es **O(log n)** porque en cada paso el tamaño del problema se reduce a la
mitad, así que la cantidad de pasos hasta llegar al caso base es la cantidad de veces que se
puede partir `n` en dos, es decir `log₂(n)`.

El archivo incluye:
- `busqueda_binaria`: la función recursiva.
- `buscar`: envoltura que reinicia el contador y devuelve el índice junto con el número de
  comparaciones.
- Un contador global de comparaciones y medición de tiempo con `time.perf_counter()`.
- Para los tamaños grandes se usa `range(n)` como arreglo ordenado, ya que permite
  indexación en O(1) sin gastar memoria en listas de millones de elementos.

#### Cómo ejecutarlo

```bash
cd 01_O_logn
python busqueda_binaria.py
```

Esto imprime:
1. Una prueba de correctitud sobre un arreglo pequeño (valores presentes y ausentes).
2. Una tabla del peor caso con `n` duplicándose desde 16 hasta 268,435,456.
3. Una tabla de tiempos promediando 20,000 búsquedas por tamaño.
4. La comparación del conteo medido contra la fórmula cerrada de la recurrencia.

#### Evidencia numérica de la complejidad

Resultado real de ejecutar `python busqueda_binaria.py` (tabla recortada, la salida completa
va de n = 16 hasta n = 268,435,456):

```
              n  comparaciones      lg(n)   comp/lg(n)   delta
   ------------------------------------------------------------
             16              5        4.0        1.250       -
             32              6        5.0        1.200      +1
             64              7        6.0        1.167      +1
            256              9        8.0        1.125      +1
          1,024             11       10.0        1.100      +1
         32,768             16       15.0        1.067      +1
      1,048,576             21       20.0        1.050      +1
     16,777,216             25       24.0        1.042      +1
    268,435,456             29       28.0        1.036      +1
```

![Ejecución del algoritmo O(log n)](docs/01_O_logn/ejecucion.png)

Evidencia de que el crecimiento es logarítmico y no lineal ni polinomial:

- Cada vez que `n` se **duplica**, el número de comparaciones sube en **exactamente +1**
  (columna `delta`). Si el algoritmo fuera O(n), al duplicar `n` el costo se duplicaría; si
  fuera O(n²) se cuadruplicaría. Subir en una unidad constante al duplicar la entrada es
  precisamente la definición de crecimiento logarítmico.
- La columna `comp/lg(n)` tiende a 1 conforme crece `n`, es decir, la razón entre el trabajo
  medido y `log₂(n)` es constante, que es lo que exige `Θ(log n)`.
- El conteo medido coincide **exacto** con `⌊lg n⌋ + 1` en todos los tamaños probados, que es
  justamente la fórmula cerrada `c(lg n + 1)` obtenida al resolver la recurrencia, con `c = 1`.
- En tiempo, al multiplicar `n` por 4 el tiempo sube apenas alrededor de 1.1×, cuando un
  algoritmo O(n) subiría 4×. Pasar de n = 64 a n = 67,108,864 (un millón de veces más datos)
  solo multiplica el tiempo por 4.

#### Relación de recurrencia y resolución

**Planteamiento.** Cada llamada genera **una sola** llamada recursiva sobre un subproblema de
la **mitad** del tamaño, y el trabajo propio de cada llamada (calcular el índice medio y hacer
la comparación) no depende de `n`:

```
T(n) = T(n/2) + c      para n > 1
T(1) = c               (caso base)
```

**Método: teorema maestro.** La recurrencia ya tiene la forma `T(n) = a·T(n/b) + f(n)` con:

- `a = 1` (una llamada recursiva)
- `b = 2` (el subproblema es de tamaño n/2)
- `f(n) = c = Θ(n⁰)`, es decir `d = 0`

Se compara `a` contra `b^d`:

```
b^d = 2⁰ = 1 = a
```

Como `a = b^d`, cae en el **segundo caso** del teorema:

```
T(n) = Θ(n^d · log n) = Θ(n⁰ · log n) = Θ(log n)
```

**Verificación por sustitución hacia atrás (desenrollado).** Tomando `n = 2^k` para que las
divisiones sean exactas y sustituyendo repetidamente:

```
T(n) = T(n/2)  + c
     = T(n/4)  + 2c
     = T(n/8)  + 3c
     ...
     = T(n/2ⁱ) + i·c
```

La recursión se detiene al llegar al caso base, o sea cuando `n/2ⁱ = 1`, y despejando eso da
`i = lg n`. Sustituyendo:

```
T(n) = T(1) + c·lg n = c + c·lg n = c(lg n + 1)
```

Por lo tanto `T(n) = Θ(log n)`, igual que por el teorema maestro.

**Verificación por ecuación característica (cambio de variable).** Como la recurrencia divide
y no resta, primero se hace el cambio `n = 2^k` y se define `S(k) = T(2^k)`. Con eso
`T(n/2) = S(k-1)` y queda una recurrencia lineal de coeficientes constantes:

```
S(k) = S(k-1) + c,    S(0) = c
```

- **Homogénea asociada:** `S(k) - S(k-1) = 0`, con ecuación característica `r - 1 = 0`, así que
  `r = 1` y `S_h(k) = A·1^k = A`.
- **Solución particular:** el término no homogéneo es la constante `c`, que se puede ver como
  `c·1^k`. Como `1` **sí** es raíz de la homogénea (multiplicidad 1), no sirve proponer una
  constante; se propone `S_p(k) = B·k`:

```
Bk = B(k-1) + c  ⟹  Bk = Bk - B + c  ⟹  B = c
```

- **Solución general:** `S(k) = A + ck`. Con `S(0) = c` se obtiene `A = c`, entonces:

```
S(k) = c(k + 1)   ⟹   T(n) = c(lg n + 1)
```

Los tres métodos coinciden y coinciden además con el conteo medido en la tabla anterior.

---

### 7. O(n!) — Generación de permutaciones

**Carpeta:** `07_O_nfactorial` · **Archivo:** `permutaciones.py` · **Responsable:** Derek Friedhelm Coronado Chilin

#### Descripción del algoritmo

El algoritmo genera **todas las permutaciones** de una lista de `n` elementos mediante
**backtracking** con intercambio de posiciones (swap). En cada nivel de la recursión se fija
un elemento en la posición actual (intercambiándolo sucesivamente con cada uno de los
elementos restantes) y se llama recursivamente para fijar el resto de posiciones; al deshacer
cada intercambio se restaura el estado para probar la siguiente opción.

Como existen exactamente `n!` permutaciones distintas de `n` elementos y el algoritmo
construye cada una exactamente una vez (sin repetir ni omitir ninguna), su complejidad en
tiempo es **O(n!)**.

El archivo incluye:
- `generar_permutaciones`: genera y devuelve todas las permutaciones (para mostrar el
  resultado concreto con `n = 4`).
- `contar_permutaciones`: recorre el mismo árbol de recursión pero solo cuenta, sin
  almacenar en memoria, para poder medir tiempos con valores de `n` más grandes.
- Un contador global de operaciones (`contador_operaciones`) y medición de tiempo con
  `time.perf_counter()`.

#### Cómo ejecutarlo

```bash
cd 07_O_nfactorial
python permutaciones.py
```

Esto imprime:
1. Las 24 permutaciones generadas para `n = 4` (para verificar que el algoritmo es correcto).
2. Una tabla con `n` de 1 a 10 mostrando: `n!`, número de permutaciones generadas, número de
   operaciones (swaps) realizadas y tiempo de ejecución.

> Toma la captura de pantalla de esta salida en la terminal y guárdala en
> `docs/07_O_nfactorial/ejecucion.png` (crea la carpeta si no existe).

#### Evidencia numérica de la complejidad

Resultado real de ejecutar `python permutaciones.py`:

```
  n |         n! |  permutaciones |  operaciones |   tiempo (s)
------------------------------------------------------------------------------
  1 |          1 |              1 |            2 |     0.000003
  2 |          2 |              2 |            6 |     0.000003
  3 |          6 |              6 |           21 |     0.000003
  4 |         24 |             24 |           88 |     0.000010
  5 |        120 |            120 |          445 |     0.000071
  6 |        720 |            720 |         2676 |     0.000312
  7 |       5040 |           5040 |        18739 |     0.002189
  8 |      40320 |          40320 |       149920 |     0.017964
  9 |     362880 |         362880 |      1349289 |     0.163118
 10 |    3628800 |        3628800 |     13492900 |     1.660010
------------------------------------------------------------------------------
```

![Ejecución del algoritmo O(n!)](docs/07_O_nfactorial/ejecucion.png)

Evidencia de que el crecimiento es factorial y no, por ejemplo, exponencial (2ⁿ) o
polinomial:

- La columna **permutaciones** coincide exactamente con **n!** para cada fila.
- La razón entre tiempos consecutivos se aproxima a `n` (el factor que multiplica a `T(n-1)`
  en la recurrencia): de `n = 9` a `n = 10`, el tiempo pasa de `0.163118 s` a `1.660010 s`,
  una razón de ≈10.18, muy cercana a `n = 10`. Este comportamiento (razón ≈ n entre pasos
  consecutivos) es característico de una función factorial y no se observa en O(2ⁿ) (donde la
  razón esperada siempre sería ≈2, constante) ni en ningún polinomio de grado fijo.
- El número de operaciones es un **múltiplo constante** de `n!`: la razón
  `operaciones / n!` se estabiliza en ≈ 3.72 desde `n = 8` en adelante
  (`149920 / 40320 = 3.718`, `1349289 / 362880 = 3.718`, `13492900 / 3628800 = 3.718`).
  Esa constante es `e + 1 ≈ 3.71828`, y aparece porque además de las `n!` hojas se cuentan
  también los nodos internos del árbol de recursión, cuyo total es
  `n!·(1 + 1/1! + 1/2! + ... ) ≈ e·n!`. Que la razón se mantenga fija confirma que el trabajo
  total es `Θ(n!)`.

#### Relación de recurrencia y resolución

**Planteamiento.** Sea `T(n)` el tiempo que toma generar todas las permutaciones de `n`
elementos. Para fijar el primer elemento, el algoritmo prueba `n` opciones (un ciclo `for`
de tamaño `n`, con trabajo `O(n)` por los intercambios), y por cada opción resuelve
recursivamente el mismo problema para los `n - 1` elementos restantes:

```
T(n) = n · T(n - 1) + c·n      para n > 1
T(1) = c                        (caso base)
```

**Método: árbol de recursión.**

- **Nivel 0** (raíz): 1 nodo, con costo `c·n`.
- **Nivel 1**: `n` nodos (uno por cada elección del primer elemento), cada uno con costo
  `c·(n-1)`. Costo del nivel: `n · c·(n-1)`.
- **Nivel 2**: `n·(n-1)` nodos, cada uno con costo `c·(n-2)`. Costo del nivel:
  `n·(n-1) · c·(n-2)`.
- En general, en el **nivel k** hay `n·(n-1)·(n-2)···(n-k+1)` nodos, cada uno con costo
  `c·(n-k)`.
- El árbol tiene `n` niveles (hasta el caso base), y en el **último nivel** (las hojas) hay
  exactamente `n · (n-1) · (n-2) ··· 1 = n!` hojas, cada una con costo constante `c`.

Sumando el costo de todos los niveles:

```
T(n) = c·n! + [suma de los costos de los niveles internos]
```

Como el número de nodos por nivel decrece de `n!` (en las hojas) hacia `n` (nivel 1), y el
costo por nodo en los niveles internos es a lo sumo `c·n`, el costo total está acotado por
arriba y por abajo por un múltiplo de `n!`:

```
c·n!  ≤  T(n)  ≤  c·n!·(1 + 1 + 1/2! + 1/3! + ... )  =  c·n!·e
```

Por lo tanto:

```
T(n) = Θ(n!)
```

**Verificación algebraica (sustitución / cambio de variable).** Dividiendo la recurrencia
`T(n) = n·T(n-1) + c·n` entre `n!` en ambos lados:

```
T(n)/n!  =  T(n-1)/(n-1)!  +  c/(n-1)!
```

Sea `S(n) = T(n)/n!`. Entonces `S(n) = S(n-1) + c/(n-1)!`, una suma telescópica:

```
S(n) = S(1) + c · Σ_{k=1}^{n-1} 1/k!
```

Como `Σ_{k=1}^{∞} 1/k! = e - 1` converge a una constante, `S(n) = O(1)`, es decir:

```
T(n) = n! · S(n) = O(n!)
```

Ambos métodos (árbol de recursión y sustitución con cambio de variable) confirman que
`T(n) = Θ(n!)`, consistente con los datos medidos en la tabla anterior.

---

### 8. O(2ⁿ) — Suma de subconjuntos (subset sum) por fuerza bruta

**Carpeta:** `08_O_2n` · **Archivo:** `algoritmo_2n.py` · **Responsable:** Angel Gabriel Sanabria Morales

#### Descripción del algoritmo

Dado un conjunto de `n` números y un valor objetivo, el algoritmo cuenta **cuántos
subconjuntos suman exactamente ese objetivo**. Recorre el conjunto elemento por elemento y en
cada uno abre **dos ramas**: una en la que el elemento se incluye en el subconjunto y otra en
la que no. A propósito no lleva poda ni memoización, pues lo que se quiere evidenciar es el
árbol de recursión completo.

La complejidad es **O(2ⁿ)** porque un conjunto de `n` elementos tiene exactamente `2ⁿ`
subconjuntos posibles y el algoritmo los recorre todos: cada elemento duplica la cantidad de
combinaciones por explorar.

Se eligió este algoritmo en lugar del Fibonacci recursivo, que es el ejemplo más común de
O(2ⁿ). La razón es que Fibonacci da la recurrencia `T(n) = T(n-1) + T(n-2) + c`, cuya solución
real es `Θ(φⁿ)` con `φ ≈ 1.618`; sí es O(2ⁿ) como cota superior, pero al medir se observarían
razones de 1.6× entre pasos consecutivos y no de 2×, lo cual debilita la evidencia numérica.
Con subset sum la recurrencia es `T(n) = 2T(n-1) + c` y el conteo medido calza exacto con la
fórmula cerrada.

El archivo incluye:
- `subset_sum`: la función recursiva que abre las dos ramas.
- `contar`: envoltura que reinicia el contador de llamadas.
- `listar_subconjuntos`: versión auxiliar que devuelve los subconjuntos encontrados, usada
  solo para verificar que el algoritmo es correcto.
- Un contador global de llamadas recursivas y medición de tiempo con `time.perf_counter()`.

#### Cómo ejecutarlo

```bash
cd 08_O_2n
python algoritmo_2n.py
```

Esto imprime:
1. Una prueba de correctitud sobre el conjunto `[3, 34, 4, 12, 5, 2]` con objetivo 9, listando
   los subconjuntos encontrados.
2. Una tabla con `n` de 1 a 20 comparando las llamadas medidas contra `2ⁿ⁺¹ - 1`.
3. Una tabla de tiempos con `n` de 14 a 24.
4. Una proyección del tiempo que tomarían tamaños mayores.

> La corrida completa tarda alrededor de 11 segundos porque llega hasta `n = 24`
> (33 millones de llamadas recursivas).

#### Evidencia numérica de la complejidad

Resultado real de ejecutar `python algoritmo_2n.py` (tabla recortada):

```
      n   hojas (2^n)       llamadas      2^(n+1)-1  coincide   razon   tiempo (s)
   --------------------------------------------------------------------------------
      4            16             31             31        SI   2.07x            -
      8           256            511            511        SI   2.00x            -
     14        16,384         32,767         32,767        SI   2.00x       0.0053
     18       262,144        524,287        524,287        SI   2.00x       0.0822
     20     1,048,576      2,097,151      2,097,151        SI   2.00x       0.3446
     22     4,194,304      8,388,607      8,388,607        SI   2.00x       1.3224
     24    16,777,216     33,554,431     33,554,431        SI   2.00x       5.3126
```

![Ejecución del algoritmo O(2ⁿ)](docs/08_O_2n/ejecucion.png)

Evidencia de que el crecimiento es exponencial base 2 y no factorial ni polinomial:

- Agregar **un solo** elemento al conjunto **duplica** el número de llamadas: la razón entre
  filas consecutivas es 2.00× en toda la tabla. Esto es lo que distingue O(2ⁿ) de O(n!), donde
  la razón crecería con `n` (2, luego 3, luego 4…) en lugar de quedarse fija en 2.
- El conteo medido coincide **exacto** con `2ⁿ⁺¹ - 1` en todos los tamaños, que es la solución
  cerrada de la recurrencia con `c = 1`. No es una aproximación: es el mismo número.
- El tiempo también se duplica al pasar de `n` a `n+1`, siguiendo el mismo patrón que el
  conteo de operaciones.
- Extrapolando a partir del tiempo medido para `n = 24`, la misma máquina tardaría alrededor
  de 4 días en `n = 40` y más de 11,000 años en `n = 60`, que es el comportamiento típico de
  un algoritmo exponencial: por más rápida que sea la computadora, cada elemento nuevo cuesta
  el doble que todo lo anterior junto.

#### Relación de recurrencia y resolución

**Planteamiento.** Cada llamada con `n` elementos pendientes genera **dos** llamadas con
`n - 1` elementos pendientes, y su trabajo propio (una resta y una suma) es constante:

```
T(n) = 2·T(n-1) + c      para n > 0
T(0) = c                  (caso base)
```

Aquí **no** aplica el teorema maestro, porque el subproblema se obtiene **restando** (`n-1`) y
no **dividiendo** (`n/b`). En cambio, sí es una recurrencia lineal de coeficientes constantes
no homogénea, así que se resuelve con ecuación característica.

**Método: ecuación característica.** Se ordena la recurrencia dejando los términos de `T` de
un lado:

```
T(n) - 2·T(n-1) = c
```

**Paso 1 — Homogénea asociada.** `T(n) - 2T(n-1) = 0`, cuya ecuación característica es:

```
r - 2 = 0   ⟹   r = 2
```

Como es una raíz simple, `T_h(n) = A·2ⁿ`.

**Paso 2 — Solución particular.** El término no homogéneo es la constante `c`, que se escribe
como `c·1ⁿ`. Como `1` **no** es raíz de la característica (la única raíz es 2), se propone una
constante `T_p(n) = B`:

```
B - 2B = c   ⟹   -B = c   ⟹   B = -c
```

**Paso 3 — Solución general.**

```
T(n) = T_h(n) + T_p(n) = A·2ⁿ - c
```

**Paso 4 — Condición inicial.** Con `T(0) = c`:

```
A·2⁰ - c = c   ⟹   A - c = c   ⟹   A = 2c
```

**Solución cerrada:**

```
T(n) = 2c·2ⁿ - c = c·(2ⁿ⁺¹ - 1) = Θ(2ⁿ)
```

**Verificación por sustitución hacia atrás (desenrollado).**

```
T(n) = 2T(n-1) + c
     = 2[2T(n-2) + c] + c = 4T(n-2) + 2c + c
     = 4[2T(n-3) + c] + 3c = 8T(n-3) + 4c + 2c + c
     ...
     = 2ⁱ·T(n-i) + c(2^(i-1) + ... + 2 + 1)
     = 2ⁱ·T(n-i) + c(2ⁱ - 1)
```

donde la parte de las constantes se sumó como serie geométrica de razón 2. El caso base se
alcanza cuando `n - i = 0`, es decir `i = n`:

```
T(n) = 2ⁿ·T(0) + c(2ⁿ - 1) = c·2ⁿ + c·2ⁿ - c = c(2ⁿ⁺¹ - 1)
```

Idéntico a lo que dio la ecuación característica, y con `c = 1` idéntico también al conteo de
llamadas medido en la tabla anterior.
