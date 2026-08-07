# Algoritmo de complejidad O(n!) — Generación de permutaciones por backtracking

import time
from math import factorial

# Contador global de operaciones "elementales" (los intercambios/swaps que
# hace el algoritmo). Se usa para medir de forma numérica cuánto trabajo
# realiza el algoritmo y compararlo contra el crecimiento teórico de n!.
contador_operaciones = 0


def generar_permutaciones(elementos, inicio=0):
    """Genera (y devuelve) todas las permutaciones de 'elementos' mediante
    backtracking con intercambio de posiciones (swap).

    Complejidad: O(n!). Existen n! permutaciones distintas de n elementos
    y el algoritmo produce cada una exactamente una vez, por lo que el
    numero de hojas del arbol de recursion es n!.
    """
    global contador_operaciones
    n = len(elementos)

    # Caso base: ya se fijó un elemento en cada posición (0..n-1), por lo
    # tanto 'elementos' es una permutación completa lista para devolver.
    if inicio == n:
        contador_operaciones += 1
        # Se copia la lista porque 'elementos' se sigue modificando (swaps)
        # en las llamadas anteriores del stack de recursión.
        return [elementos.copy()]

    resultado = []
    # Se prueba, uno por uno, cada elemento restante (desde 'inicio' hasta
    # el final) como candidato para ocupar la posición 'inicio'.
    for i in range(inicio, n):
        contador_operaciones += 1
        # Se coloca el elemento i en la posición 'inicio' mediante swap.
        elementos[inicio], elementos[i] = elementos[i], elementos[inicio]

        # Se resuelve recursivamente el mismo problema para las posiciones
        # restantes (inicio + 1 .. n - 1); esta es la parte que hace que el
        # algoritmo ramifique en n, luego n-1, luego n-2, ... opciones.
        resultado.extend(generar_permutaciones(elementos, inicio + 1))

        # Se deshace el swap (backtrack) para restaurar el orden original
        # antes de probar el siguiente candidato en la posición 'inicio'.
        elementos[inicio], elementos[i] = elementos[i], elementos[inicio]

    return resultado


def contar_permutaciones(elementos, inicio=0):
    """Version que solo cuenta las permutaciones (no las almacena en memoria).

    Recorre exactamente el mismo arbol de recursion que generar_permutaciones,
    por lo que conserva la complejidad de tiempo O(n!); se usa para medir
    tiempos con valores de n mas grandes sin agotar memoria.
    """
    global contador_operaciones
    n = len(elementos)

    # Caso base: se completó una permutación; se cuenta como 1 en vez de
    # copiarla y almacenarla (por eso esta versión gasta menos memoria).
    if inicio == n:
        contador_operaciones += 1
        return 1

    total = 0
    for i in range(inicio, n):
        contador_operaciones += 1
        elementos[inicio], elementos[i] = elementos[i], elementos[inicio]
        # Se suman los conteos de todas las ramas hijas.
        total += contar_permutaciones(elementos, inicio + 1)
        elementos[inicio], elementos[i] = elementos[i], elementos[inicio]

    return total


def medir(n):
    """Mide, para una lista de tamaño n, el tiempo de ejecución, el total de
    permutaciones encontradas, el valor teórico n! y el número de
    operaciones (swaps) realmente ejecutadas.
    """
    global contador_operaciones
    contador_operaciones = 0
    datos = list(range(1, n + 1))

    inicio = time.perf_counter()
    total = contar_permutaciones(datos)
    fin = time.perf_counter()

    return fin - inicio, total, factorial(n), contador_operaciones


def main():
    print("=" * 78)
    print(" ALGORITMO O(n!) - GENERACION DE PERMUTACIONES (backtracking)")
    print("=" * 78)

    # Primero se muestra un ejemplo concreto (n = 4) para verificar
    # visualmente que el algoritmo genera permutaciones válidas y completas.
    print("\nEjemplo de permutaciones generadas para n = 4:")
    ejemplo = generar_permutaciones([1, 2, 3, 4])
    for p in ejemplo:
        print(p)
    print(f"Total generado: {len(ejemplo)}  |  4! = {factorial(4)}")

    # Luego se mide el algoritmo para n = 1..10 y se compara contra n!,
    # para evidenciar numéricamente que el crecimiento es factorial.
    print("\nEvidencia numerica de la complejidad O(n!):")
    print(f"{'n':>3} | {'n!':>10} | {'permutaciones':>14} | {'operaciones':>12} | {'tiempo (s)':>12}")
    print("-" * 78)

    for n in range(1, 11):
        tiempo, total, nf, ops = medir(n)
        print(f"{n:>3} | {nf:>10} | {total:>14} | {ops:>12} | {tiempo:>12.6f}")

    print("-" * 78)
    print("La columna 'permutaciones' coincide exactamente con n!, y el numero")
    print("de operaciones y el tiempo de ejecucion crecen a un ritmo factorial")
    print("conforme n aumenta, lo que evidencia numericamente la complejidad O(n!).")


if __name__ == "__main__":
    main()
