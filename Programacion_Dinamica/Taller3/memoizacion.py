from pprint import pprint

def PSC(s: str) -> int:
    n = len(s)
    # Inicializar matriz n x n con -1, y 1 en la diagonal
    M = [[1 if i == j else -1 for i in range(n)] for j in range(n)]
    total = PSC_AUX(s, 0, n - 1, M)

    print(f"String: {s!r} | Total subsecuencias palíndromas = {total}")
    pprint(M)
    return total


def PSC_AUX(s: str, i: int, j: int, M: list[list[int]]) -> int:
    if i > j:
        return 0
    if M[i][j] != -1:
        return M[i][j]

    if s[i].lower() == s[j].lower():
        ans = PSC_AUX(s, i + 1, j, M) + PSC_AUX(s, i, j - 1, M) + 1
    else:
        ans = (PSC_AUX(s, i + 1, j, M) +
               PSC_AUX(s, i, j - 1, M) -
               PSC_AUX(s, i + 1, j - 1, M))

    M[i][j] = ans
    return ans

if __name__ == "__main__":
    # Pruebas
    PSC("Amapola")   # esperado: 19
    PSC("panaa")   # esperado: 11
    PSC("lana")    # esperado: 6
    PSC("aro")     # esperado: 3
