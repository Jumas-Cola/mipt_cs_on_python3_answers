def upd_cell():
    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            if cell[i][j] == '-':
                if i>0: cell[i-1][j] = '+'
                if j>0: cell[i][j-1] = '+'
                if i>0 and j>0: cell[i-1][j-1] = '+'
            if cell[i][j] == ' ' and i < N-1 and j < M-1 and (cell[i+1][j] == '+' or i+1 > N-1) and (cell[i][j+1] == '+' or j+1 > M-1) and (cell[i+1][j+1] == '+' or (i+1 > N-1 and j+1 > M-1)):
                cell[i][j] = '-'

M = 8
N = 6
cell = [[' ' for j in range(M)] for i in range(N)]

cell[N-1][M-1] = '-'

while 1:
    filled = 1
    for i in cell:
        if ' ' in i:
            upd_cell()
            filled = 0
    if filled:
        break

for i in cell:
    print(i)
