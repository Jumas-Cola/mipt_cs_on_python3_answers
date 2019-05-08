M = 6
N = 8
cell = [[' ' for j in range(M)] for i in range(N)]

cell[N - 1][M - 1] = '-'

for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if cell[i][j] == ' ':
            if j + 1 == M and i + 1 != N and cell[i + 1][j] == '+':
                cell[i][j] = '-'
            elif i + 1 == N and j + 1 != M and cell[i][j + 1] == '+':
                cell[i][j] = '-'
        try:
            if cell[i][j + 1] == cell[i + 1][j] == cell[i + 1][j + 1] == '+':
                cell[i][j] = '-'
        except:
            pass
        if cell[i][j] == '-':
            if i > 0:
                cell[i - 1][j] = '+'
            if j > 0:
                cell[i][j - 1] = '+'
            if i > 0:
                cell[i - 1][j] = '+'
            if j > 0 and i > 0:
                cell[i - 1][j - 1] = '+'

for i in cell:
    print(i)
