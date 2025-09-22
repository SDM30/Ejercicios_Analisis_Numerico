import pprint

def CHAIN_MATRIX(D):
    # D = [d0, d1, ..., dn], Ai es d_{i-1} x d_i
    n = len(D) - 1
    # M[i][j] guarda el costo óptimo de Ai..Aj (i,j en 1..n)
    M = [[0 if i == j else float('inf') for j in range(n + 1)]
         for i in range(n + 1)]
    return CHAIN_MATRIX_AUX(D, 1, n, M), pprint.pprint(M)

def CHAIN_MATRIX_AUX(D, i, j, M):
    # Si ya está calculado, sacarlo de la matriz
    if M[i][j] != float('inf'):
        return M[i][j]

    q = float('inf')
    for k in range(i, j):
        v  = CHAIN_MATRIX_AUX(D, i, k, M)
        v += CHAIN_MATRIX_AUX(D, k + 1, j, M)
        v += D[i - 1] * D[k] * D[j]
        if v < q:
            q = v

    M[i][j] = q
    return q

if __name__=="__main__":
    # Pruebas
    D = [5, 100, 20, 4]        # A1: 5x100, A2: 100x20, A3: 20x4
    print(CHAIN_MATRIX(D))     # 10000

    D = [10, 100, 5, 50]
    print(CHAIN_MATRIX(D))     # 7500
