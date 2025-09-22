import pprint
def MATRIX_CHAIN_ORDER(D):
    # 1  n = p.length - 1
    n = len(D) - 1

    # 2  let m[1..n,1..n] and s[1..n-1,2..n] be new tables
    m = [[0]*(n+1) for _ in range(n+1)]
    s = [[0]*(n+1) for _ in range(n+1)]

    # 3  for i = 1 to n
    for i in range(1, n+1):
        # 4      m[i,i] = 0
        m[i][i] = 0

    # 5  for l = 2 to n          // l is the chain length
    for l in range(2, n+1):
        # 6      for i = 1 to n - l + 1
        for i in range(1, n - l + 2):
            # 7          j = i + l - 1
            j = i + l - 1
            # 8          m[i,j] = ∞
            m[i][j] = float('inf')
            # 9          for k = i to j - 1
            for k in range(i, j):
                # 10             q = m[i,k] + m[k+1,j] + p_{i-1} p_k p_j
                q = m[i][k] + m[k+1][j] + D[i-1] * D[k] * D[j]
                # 11             if q < m[i,j]
                if q < m[i][j]:
                    # 12                 m[i,j] = q
                    m[i][j] = q
                    # 13                 s[i,j] = k
                    s[i][j] = k

    # 14 return m and s
    return m, s

def PRINT_OPTIMAL_PARENS(s, i, j):
    if i == j:
        return f"A{i}"
    k = s[i][j]            # k está en [i, j-1]
    left  = PRINT_OPTIMAL_PARENS(s, i, k)
    right = PRINT_OPTIMAL_PARENS(s, k + 1, j)
    return f"({left}{right})"


if __name__=="__main__":
    D = [10, 100, 5, 50]
    m, s = MATRIX_CHAIN_ORDER(D)
    pprint.pprint(m)
    pprint.pprint(s)
    n = len(D) - 1 
    print(PRINT_OPTIMAL_PARENS(s,1,n))