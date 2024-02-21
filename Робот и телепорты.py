def calc_weg(x: int, y: int) -> [int, int]:
    max_weg = 0
    max_step = 0
    if (board[x-1][y][1]+board[x][y][0])/(board[x-1][y][2]+1) > (board[x][y-1][1]+board[x][y][0])/(board[x][y-1][2]+1):
        max_weg = board[x-1][y][1]+board[x][y][0]
        max_step = board[x-1][y][2]+1
    else:
        max_weg = board[x][y-1][1]+board[x][y][0]
        max_step = board[x][y-1][2]+1
    return [max_weg, max_step]


n, m, k = map(int, input().split())

tel = []

for i in range(k):
    tel.append(tuple(map(int, input().split())))

board = [[[0, 0, 0] * (n+1)]] + [[[0, 0, 0] + [[0, 0, 1]] * m]] * n

print()
print(board)
print()

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        board[i+1][j+1][0] = a[j]



for i in range(1, n+1):
    for j in range(1, m+1):
        board[i][j][1], board[i][j][2] = calc_weg(i, j)


for l in range(len(tel)):
    max_weg = board[tel[l][0]][tel[l][1]][1]
    max_step = board[tel[l][0]][tel[l][1]][2]
    for t in range(len(tel)):
        if t == l:
            if max_weg/max_step < (board[tel[l][0]][tel[l][1]][1] + board[tel[l][0]][tel[l][1]][0])/(max_step+1):
                max_weg = board[tel[l][0]][tel[l][1]][1] + board[tel[l][0]][tel[l][1]][0]
                max_step += 1
        else:
            if max_weg/max_step < (board[tel[t][0]][tel[t][1]][1]+board[tel[l][0]][tel[l][1]][0])/(board[tel[t][0]][tel[t][1]][2]+1):
                max_weg = board[tel[t][0]][tel[t][1]][1]+board[tel[l][0]][tel[l][1]][0]
                max_step = board[tel[t][0]][tel[t][1]][2]+1
    if max_weg/max_step > board[tel[l][0]][tel[l][1]][1]/board[tel[l][0]][tel[l][1]][2]:


        small_board = [[[0, 0, 0]]*(m+1-tel[l][1])]
        for i in range(tel[l][0]):
            small_board.append([[0, 0, 0]] + board[i][tel[l][1]:len(board[i])])
        small_board[1][1][1], small_board[1][1][2] = max_weg, max_step
        
        for i in range(1, n+1-tel[l][0]):
            for j in range(1, m+1-tel[l][1]):
                if (small_board[i-1][j][1]+small_board[i][j][0])/(small_board[i-1][j][2]+1) > (small_board[i][j-1][1]+small_board[i][j][2])/(small_board[i][j-1][2]+1):
                    small_board[i][j][1] = small_board[i-1][j][1]+small_board[i][j][0]
                    small_board[i][j][2] = small_board[i-1][j][2]+1
                else:
                    small_board[i][j][1] = small_board[i][j-1][1]+small_board[i][j][2]
                    small_board[i][j][2] = small_board[i][j-1][2]+1
        if small_board[len(small_board)-1][len(small_board[0])-1][1]/small_board[len(small_board)-1][len(small_board[0])-1][2] > board[n+1][m+1][1]/board[n+1][m+1][2]:
            board[n+1][m+1][1] = small_board[len(small_board)][len(small_board[0])][1]
            board[n+1][m+1][2] = small_board[len(small_board)][len(small_board[0])][2]


print(board[n+1][m+1][1]/board[n+1][m+1][2])
