import math
import time
import random
import sys
from typing import List

# permitir hasta 30,000 dígitos (Python 3.11+)
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(30000)

_ALPHABET = "0123456789ABCDEF"

# -------------------------------
# Conversión exhaustiva
# -------------------------------
def length_digits(n: int, b: int) -> int:
    """Calcula cuántos dígitos ocupa n en base b."""
    if n == 0:
        return 1
    return math.floor(math.log(n, b)) + 1

def ConvertirBaseInversa(n: int, b: int) -> List[str]:
    """
    Convierte el entero n a base b de forma exhaustiva,
    retornando los dígitos en orden inverso (LSD -> MSD).
    Si un dígito es >=10, se mapea a letra (A..F).
    """
    d = length_digits(n, b)
    R = [None] * d
    i = 0
    j = d - 1
    for _ in range(d):
        digit = (n // (b ** i)) % b
        R[j] = _ALPHABET[digit]
        i += 1
        j -= 1
    return R[::-1]

# -------------------------------
# Prueba aleatoria
# -------------------------------
def test_random(num_tests: int = 20, max_n: int = 100000) -> None:
    """
    Genera pruebas aleatorias para ConvertirBaseInversa.
    Mide el tiempo total y reporta el tamaño máximo de entrada.
    """
    start = time.perf_counter()
    max_digits = 0

    for _ in range(num_tests):
        n = random.randint(1, max_n)   # evitar n=0
        b = random.randint(2, 16)

        # calcular representación inversa
        _ = ConvertirBaseInversa(n, b)

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

# -------------------------------
# Main
# -------------------------------
def main():
    if len(sys.argv) != 3:
        print("Uso: python tu_script.py <numero> <base>")
        sys.exit(1)

    n = int(sys.argv[1])
    b = int(sys.argv[2])

    if n < 0:
        print("El número debe ser >= 0.")
        sys.exit(1)
    if not (2 <= b <= 16):
        print("La base debe estar entre 2 y 16.")
        sys.exit(1)

    tam = length_digits(n, b)
    start = time.perf_counter()
    inv = ConvertirBaseInversa(n, b)
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
