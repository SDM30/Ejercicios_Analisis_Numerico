def CHAIN_MATRIX(D):
    # D = [d0, d1, ..., dn], Ai is d_{i-1} x d_i
    n = len(D) - 1
    return CHAIN_MATRIX_AUX(D, 1, n)

def CHAIN_MATRIX_AUX(D, i, j):
    if i == j:
        return 0
    q = float('inf')
    for k in range(i, j):
        v  = CHAIN_MATRIX_AUX(D, i, k)
        v += CHAIN_MATRIX_AUX(D, k + 1, j)
        v += D[i - 1] * D[k] * D[j]   # cost of final multiply
        if v < q:
            q = v
    return q

if __name__=="__main__":
    # test
    D = [5, 100, 20, 4]   # A1: 5x100, A2: 100x20, A3: 20x4
    print(CHAIN_MATRIX(D))  # -> 10000
    D = [10,100,5,50]
    print(CHAIN_MATRIX(D))  

