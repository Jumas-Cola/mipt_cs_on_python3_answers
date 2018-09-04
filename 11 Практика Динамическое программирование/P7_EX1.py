def kuz(n):
    F = [-1]*(n+1)
    F[0] = 0
    F[1] = 1
    F[2] = F[0] + F[1]
    for i in range(3, n+1):
        F[i] = F[i - 1] + F[i - 2] + F[i - 3]
    return F[n]

print(kuz(4))