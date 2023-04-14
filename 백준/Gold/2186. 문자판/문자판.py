import sys
n, m, k = map(int, input().split())
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(input().rstrip())

answer = list(input().rstrip())
check = [[[-1] * len(answer) for _ in range(m)] for _ in range(n)]


def dfs(x, y, index, target, k):
    global cnt
    if index == len(target):
        return 1
    if check[x][y][index] != -1:
        return check[x][y][index]

    check[x][y][index] = 0
    for i in range(1, k+1):
        for d in range(4):
            nx = x + dx[d] * i
            ny = y + dy[d] * i
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if board[nx][ny] == target[index]:
                    check[x][y][index] += dfs(nx, ny, index + 1, target, k)

    return check[x][y][index]


cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == answer[0]:
            cnt += dfs(i, j, 1, answer, k)


print(cnt)