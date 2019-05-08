
M = 8
N = 8
cell = [[' ' for j in range(M)] for i in range(N)]
cell[N - 1][M - 1] = '-'

for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if cell[i][j] == ' ' and i < N - 1 and j < M - 1 and cell[i + 1][j] == cell[i][j + 1] == cell[i + 1][j + 1] == '+':
            cell[i][j] = '-'
        if cell[i][j] == '-':
            for k in range(i, 0, -1):
                cell[k - 1][j] = '+'
            for k in range(j, 0, -1):
                cell[i][k - 1] = '+'
            s, r = i, j
            while s and r:
                cell[s - 1][r - 1] = '+'
                s -= 1
                r -= 1

for i in cell:
    print(i)
