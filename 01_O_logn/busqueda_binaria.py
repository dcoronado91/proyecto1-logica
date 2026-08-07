import sys
import time
from math import log2, floor

sys.setrecursionlimit(10000)

comparaciones = 0  # contador global de llamadas recursivas efectivas


def busqueda_binaria(arr, objetivo, izq, der):
    """Busca 'objetivo' en arr[izq..der]. Devuelve el indice o -1."""
    global comparaciones

    if izq > der:            # caso base: subarreglo vacio
        return -1

    comparaciones += 1       # trabajo constante: 1 comparacion por nivel
    medio = (izq + der) // 2

    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria(arr, objetivo, medio + 1, der)   # T(n/2)
    else:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)   # T(n/2)


def buscar(arr, objetivo):
    """Envoltura: reinicia el contador y lanza la busqueda."""
    global comparaciones
    comparaciones = 0
    indice = busqueda_binaria(arr, objetivo, 0, len(arr) - 1)
    return indice, comparaciones


# ----------------------------------------------------------------------
# EVIDENCIA NUMERICA
# ----------------------------------------------------------------------
def evidencia():
    print("=" * 74)
    print("  BUSQUEDA BINARIA  ->  T(n) = T(n/2) + c  ->  O(lg n)")
    print("=" * 74)

    # --- Prueba de correctitud -----------------------------------------
    arr = list(range(0, 200, 2))          # [0, 2, 4, ..., 198]
    print("\n1) Prueba de correctitud (arreglo de 100 pares: 0,2,4,...,198)")
    for objetivo in (0, 86, 198, 87):
        idx, comps = buscar(arr, objetivo)
        estado = f"encontrado en indice {idx}" if idx != -1 else "NO esta en el arreglo"
        print(f"   buscar({objetivo:>3}) -> {estado:<28} | comparaciones = {comps}")

    # --- Crecimiento de las comparaciones ------------------------------
    # Se usa range(n) como arreglo ordenado: indexacion O(1) y sin gastar RAM.
    # Peor caso: buscar el valor n (mayor que todos) obliga a recorrer la rama
    # mas larga del arbol de recursion.
    print("\n2) Peor caso: comparaciones al ir duplicando n")
    print(f"\n   {'n':>12} {'comparaciones':>14} {'lg(n)':>10} {'comp/lg(n)':>12} {'delta':>7}")
    print("   " + "-" * 60)

    anterior = None
    for k in range(4, 29):
        n = 2 ** k
        arr = range(n)                    # arreglo ordenado 0..n-1
        _, comps = buscar(arr, n)         # n no existe -> peor caso
        delta = "-" if anterior is None else f"+{comps - anterior}"
        print(f"   {n:>12,} {comps:>14} {log2(n):>10.1f} {comps / log2(n):>12.3f} {delta:>7}")
        anterior = comps

    print("\n   Lectura: cada vez que n se DUPLICA, las comparaciones suben en")
    print("   exactamente +1. Ese es el comportamiento logaritmico: el numero de")
    print("   comparaciones es floor(lg n) + 1, y comp/lg(n) tiende a 1 (constante).")
    print("   Si fuera O(n), al duplicar n el costo se duplicaria, no subiria en 1.")

    print("\n3) Tiempo de ejecucion (promedio de 20,000 busquedas por tamano)")
    print(f"\n   {'n':>12} {'tiempo (us)':>14} {'tiempo/lg(n)':>14} {'razon al x4 n':>16}")
    print("   " + "-" * 60)

    reps = 20_000
    t_anterior = None
    for k in range(6, 27, 2):
        n = 2 ** k
        arr = range(n)
        inicio = time.perf_counter()
        for _ in range(reps):
            busqueda_binaria(arr, n, 0, n - 1)
        fin = time.perf_counter()
        t = (fin - inicio) / reps * 1e6              # microsegundos por busqueda
        razon = "-" if t_anterior is None else f"{t / t_anterior:.2f}x"
        print(f"   {n:>12,} {t:>14.3f} {t / log2(n):>14.4f} {razon:>16}")
        t_anterior = t

    print("\n   Lectura: cada fila multiplica n por 4. Si el algoritmo fuera O(n)")
    print("   el tiempo se multiplicaria por 4 en cada fila; aqui apenas sube un")
    print("   poco, y la columna tiempo/lg(n) se queda practicamente constante.")

    # --- Comprobacion contra la formula cerrada -------------------------
    print("\n4) Comparacion contra la solucion de la recurrencia: T(n) = c*(lg n + 1)")
    print(f"\n   {'n':>12} {'medido':>10} {'floor(lg n)+1':>15} {'coincide':>10}")
    print("   " + "-" * 51)
    for k in (10, 15, 20, 25, 28):
        n = 2 ** k
        _, comps = buscar(range(n), n)
        teorico = floor(log2(n)) + 1
        print(f"   {n:>12,} {comps:>10} {teorico:>15} {'SI' if comps == teorico else 'NO':>10}")

    print("\n" + "=" * 74)
    print("  CONCLUSION: el algoritmo ejecuta floor(lg n) + 1 comparaciones,")
    print("  por lo tanto T(n) = O(lg n).")
    print("=" * 74)


if __name__ == "__main__":
    evidencia()