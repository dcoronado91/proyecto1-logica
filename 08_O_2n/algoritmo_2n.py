import sys
import time

sys.setrecursionlimit(10000)

llamadas = 0  # contador global de llamadas recursivas


def subset_sum(conjunto, i, restante):
    """Cuenta los subconjuntos de conjunto[i:] cuya suma es 'restante'."""
    global llamadas
    llamadas += 1                       # trabajo constante c

    if i == len(conjunto):              # caso base: ya no quedan elementos
        return 1 if restante == 0 else 0

    incluir = subset_sum(conjunto, i + 1, restante - conjunto[i])   # T(n-1)
    excluir = subset_sum(conjunto, i + 1, restante)                 # T(n-1)
    return incluir + excluir


def contar(conjunto, objetivo):
    """Envoltura: reinicia el contador y lanza la busqueda."""
    global llamadas
    llamadas = 0
    resultado = subset_sum(conjunto, 0, objetivo)
    return resultado, llamadas


# Version que ademas devuelve los subconjuntos, solo para la demostracion visual
def listar_subconjuntos(conjunto, objetivo, i=0, actual=None, encontrados=None):
    if actual is None:
        actual, encontrados = [], []
    if i == len(conjunto):
        if sum(actual) == objetivo:
            encontrados.append(list(actual))
        return encontrados
    actual.append(conjunto[i])
    listar_subconjuntos(conjunto, objetivo, i + 1, actual, encontrados)
    actual.pop()
    listar_subconjuntos(conjunto, objetivo, i + 1, actual, encontrados)
    return encontrados


# ----------------------------------------------------------------------
# EVIDENCIA NUMERICA
# ----------------------------------------------------------------------
def evidencia():
    print("=" * 78)
    print("  SUMA DE SUBCONJUNTOS  ->  T(n) = 2T(n-1) + c  ->  O(2^n)")
    print("=" * 78)

    # --- Prueba de correctitud -----------------------------------------
    conjunto = [3, 34, 4, 12, 5, 2]
    objetivo = 9
    resultado, calls = contar(conjunto, objetivo)
    print(f"\n1) Prueba de correctitud")
    print(f"   conjunto = {conjunto}   objetivo = {objetivo}")
    print(f"   subconjuntos que suman {objetivo}: {resultado}")
    for s in listar_subconjuntos(conjunto, objetivo):
        print(f"      {s}  ->  suma {sum(s)}")
    print(f"   llamadas recursivas = {calls}   (2^(6+1) - 1 = {2 ** 7 - 1})")

    # --- Conteo de llamadas contra la formula cerrada -------------------
    print("\n2) Llamadas recursivas contra la solucion de la recurrencia")
    print(f"\n   {'n':>4} {'hojas (2^n)':>13} {'llamadas':>14} {'2^(n+1)-1':>14} "
          f"{'coincide':>9} {'razon':>7}")
    print("   " + "-" * 68)

    anterior = None
    for n in range(1, 21):
        conjunto = list(range(1, n + 1))
        objetivo = 10 ** 9                      # nadie lo alcanza: arbol completo
        _, calls = contar(conjunto, objetivo)
        teorico = 2 ** (n + 1) - 1
        razon = "-" if anterior is None else f"{calls / anterior:.2f}x"
        print(f"   {n:>4} {2 ** n:>13,} {calls:>14,} {teorico:>14,} "
              f"{'SI' if calls == teorico else 'NO':>9} {razon:>7}")
        anterior = calls

    print("\n   Lectura: agregar UN solo elemento al conjunto DUPLICA el numero de")
    print("   llamadas (razon = 2.00x en toda la tabla) y el conteo medido calza")
    print("   exacto con 2^(n+1) - 1, que es la solucion de T(n) = 2T(n-1) + c.")

    # --- Tiempos --------------------------------------------------------
    print("\n3) Tiempo de ejecucion")
    print(f"\n   {'n':>4} {'llamadas':>14} {'tiempo (s)':>12} {'razon t(n)/t(n-1)':>19}")
    print("   " + "-" * 53)

    t_anterior = None
    for n in range(14, 25):
        conjunto = list(range(1, n + 1))
        inicio = time.perf_counter()
        _, calls = contar(conjunto, 10 ** 9)
        t = time.perf_counter() - inicio
        razon = "-" if t_anterior is None else f"{t / t_anterior:.2f}x"
        print(f"   {n:>4} {calls:>14,} {t:>12.4f} {razon:>19}")
        t_anterior = t

    print("\n   Lectura: el tiempo tambien se duplica al pasar de n a n+1. Eso es")
    print("   crecimiento exponencial base 2: no importa que tan rapida sea la")
    print("   maquina, cada elemento nuevo cuesta el doble que todo lo anterior.")

    # --- Por que es intratable ------------------------------------------
    print("\n4) Proyeccion (a partir del tiempo medido para n = 24)")
    base = t_anterior / (2 ** 24)                 # segundos por llamada aprox.
    print(f"\n   {'n':>4} {'llamadas estimadas':>22} {'tiempo estimado':>22}")
    print("   " + "-" * 50)
    for n in (30, 40, 50, 60):
        calls = 2 ** (n + 1) - 1
        seg = base * 2 ** n
        if seg < 3600:
            legible = f"{seg:.1f} s"
        elif seg < 86400 * 365:
            legible = f"{seg / 86400:.1f} dias"
        else:
            legible = f"{seg / (86400 * 365):,.0f} anios"
        print(f"   {n:>4} {calls:>22,} {legible:>22}")

    print("\n" + "=" * 78)
    print("  CONCLUSION: llamadas(n) = 2^(n+1) - 1 = 2*2^n - 1, por lo tanto")
    print("  T(n) = O(2^n).")
    print("=" * 78)


if __name__ == "__main__":
    evidencia()