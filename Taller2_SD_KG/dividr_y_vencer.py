import math
import time
import random
import argparse
import sys
from typing import List

# permitir hasta 30,000 dígitos (Python 3.11+)
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(30000)

_ALPHABET = "0123456789ABCDEF"

# ---------------- Funciones base ----------------

def length_digits(n: int, b: int) -> int:
    """Calcula cuántos dígitos ocupa n en base b."""
    if n == 0:
        return 1
    return int(math.floor(math.log(n, b)) + 1)

def ConvertBaseDACInverse(n: int, b: int) -> List[str]:
    """
    Convierte el entero n a base b usando Divide & Conquer
    y retorna la secuencia de dígitos en ORDEN INVERSO (LSD -> MSD).
    Los dígitos se devuelven como strings (0–9, A–F).
    Precondición: n >= 0, 2 <= b <= 16
    """
    assert n >= 0 and 2 <= b <= 16

    # Caso base: un solo dígito
    if n < b:
        return [_ALPHABET[n]]

    # Elección de pivote
    d = length_digits(n, b)
    m = d // 2
    M = b ** m

    # Partición
    high = n // M
    low  = n % M

    # Recursión
    H = ConvertBaseDACInverse(high, b)   # inverso
    L = ConvertBaseDACInverse(low,  b)   # inverso

    # Padding: asegurar que 'low' ocupe exactamente m dígitos
    need = m - length_digits(low, b)
    for _ in range(max(0, need)):
        L.append("0")  # en inverso, ceros al FINAL

    # Combinar en inverso: low primero, luego high
    return L + H

# ---------------- Prueba aleatoria ----------------

def test_random(num_tests: int = 20, max_n: int = 100000) -> None:
    """
    Genera pruebas aleatorias para ConvertBaseDACInverse.
    Mide el tiempo total y reporta el tamaño máximo de entrada.
    """
    start = time.perf_counter()
    max_digits = 0

    for _ in range(num_tests):
        n = random.randint(1, max_n)
        b = random.randint(2, 16)

        # calcular representación inversa
        _ = ConvertBaseDACInverse(n, b)

        # medir tamaño de entrada
        d = length_digits(n, b)
        if d > max_digits:
            max_digits = d

    end = time.perf_counter()
    total_time = end - start

    # Fila de resultados
    print(
        f"{num_tests:<15}{length_digits(max_n, 10):<20}{max_digits:<20}{total_time:<20.6f}"
    )

# ---------------- Main ----------------

def main():
    parser = argparse.ArgumentParser(
        description="Convierte un número a base b (Divide & Conquer). Devuelve dígitos en orden inverso."
    )
    parser.add_argument("numero", type=int, help="Número entero (>= 0)")
    parser.add_argument("base", type=int, help="Base destino (2..16)")
    args = parser.parse_args()

    n, b = args.numero, args.base
    if n < 0:
        parser.error("El número debe ser >= 0.")
    if not (2 <= b <= 16):
        parser.error("La base debe estar entre 2 y 16.")

    tam = length_digits(n, b)
    start = time.perf_counter()
    inv = ConvertBaseDACInverse(n, b)
    end = time.perf_counter()
    salida = len(inv)
    t = end - start

    print(f"Tamaño entrada: {tam} dígitos -> Salida: {salida} dígitos | Tiempo: {t:.6f} seg")
    print(f"Resultado inverso: {inv}")

if __name__ == "__main__":
    main()

    # Encabezado de tabla
    # print(
    #     f"{'Pruebas':<15}{'Entrada máx':<20}{'Salida máx':<20}{'Tiempo total (s)':<20}"
    # )
    # print("-" * 75)
    # test_random(100, 10**100)        # Números de 100 dígitos
    # test_random(100, 10**1000)       # Números de 1000 dígitos
    # test_random(100, 10**10000)      # Números de 10000 dígitos
