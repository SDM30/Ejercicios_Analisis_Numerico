def CUT_ROD(P, n):
    # let r[0..n] be a sequence
    r = [0] * (n + 1)
    # let s[0..n] be a sequence
    s = [0] * (n + 1)

    # r[0] ← 0
    r[0] = 0

    # for j ← 1 to n do
    for j in range(1, n + 1):
        # r[j] ← -∞
        r[j] = float("-inf")

        # for i ← 1 to j do
        for i in range(1, j + 1):
            # v ← P[i] + r[j - i]
            v = P[i] + r[j - i]

            # if r[j] < v then
            if r[j] < v:
                # r[j] ← v
                r[j] = v

                # s[j] ← i
                s[j] = i

    #Backtracking
    m = n
    t = []
    while m > 0:
        t.append(s[m])
        m = m - s[m]
    
    print(r)
    print(s)

    # return r[n]
    return r[n], t

if __name__=="__main__":
    P=[0,1,5,8,9,10,17,17,20,24,30]
    n=4
    print(CUT_ROD(P,n))
