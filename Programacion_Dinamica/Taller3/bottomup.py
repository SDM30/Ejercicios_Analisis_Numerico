from pprint import pprint

def PSC(s: str) -> int:
    
    t = ''.join(ch.lower() for ch in s if ch.isalpha())
    n = len(t)
    if n == 0:
        print("String vacío -> 0")
        return 0

    # M[i][j] = P(i,j). Iniciamos todo en 0 y ponemos la diagonal en 1.
    M = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = 1  # P(i,i)=1

    # l = longitud del intervalo (de 2 hasta n)
    for l in range(2, n+1):
        # i = indice de la fila
        for i in range(0, n - l + 1):
            j = i + l - 1
            if t[i] == t[j]:
                M[i][j] = M[i+1][j] + M[i][j-1] + 1
            else:
                # Si i+1 > j-1, entonces cross = 0 
                cross = M[i+1][j-1] if (i + 1) <= (j - 1) else 0
                M[i][j] = M[i+1][j] + M[i][j-1] - cross

    total = M[0][n-1]
    print(f"String: {s!r} | Total subsecuencias palíndromas = {total}")
    # pprint(M, width=120)
    return total

if __name__ == "__main__":
    PSC("Amapola")  # esperado (case-insensitive): 19
    PSC("panaa")    # 11
    PSC("lana")     # 6
    PSC("aro")      # 3

    #Primera estrofa del himno nacional de locombia
    PSC(
        """
        Cesó la horrible noche
        La libertad sublime
        Derrama las auroras
        De su invencible luz
        La humanidad entera
        Que entre cadenas gime
        Comprende las palabras
        Del que murió en la cruz
        """
    )
    # Coro
    PSC(
        """
        Oh gloria inmarcesible 
        Oh júbilo inmortal 
        En surcos de dolores 
        El bien germina ya. 
        """
    )
