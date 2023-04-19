import sys
from collections import deque

# 흰색인 경우에 왼쪽부터 빼서 오른쪽에 추가한다.
# 빨간색인 경우 오른쪽에서 빼서 오른쪽에 추가한다.
# 파란색인경우 이동 위치가 파란색이면 방향만 바꾼다. 만약 다른색깔이면 위의 경우를 따르면서 한칸 이동한다.
# 체스판을 벗어나면 그냥 방향만 바꾼다.


class Horse:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = -1


n, k = map(int, input().rstrip().split())
board = [[] for _ in range(n)]
boardInfo = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        boardInfo[i][j] = deque()
Horses = [Horse] * (k+1)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    board[i] = list(map(int, input().rstrip().split()))


horseInfo = [0] * (k+1)

index = 1
for i in range(k):
    temp = list(map(int, input().rstrip().split()))
    horse = Horse()
    horse.x = temp[0] - 1
    horse.y = temp[1] - 1
    horse.direction = temp[2] - 1
    horse.index = index
    horseInfo[index] = horse
    boardInfo[temp[0]-1][temp[1]-1].append(index)
    index += 1

turn = 0
answer = -1
maxLen = -1
stopFlag = False


def white(x, y, nx, ny):
    while boardInfo[x][y]:
        index = boardInfo[x][y].popleft()
        horseInfo[index].x = nx
        horseInfo[index].y = ny
        boardInfo[nx][ny].append(index)


def red(x, y, nx, ny):
    while boardInfo[x][y]:
        index = boardInfo[x][y].pop()
        horseInfo[index].x = nx
        horseInfo[index].y = ny
        boardInfo[nx][ny].append(index)


def change(direction):
    if direction == 0:
        return 1
    elif direction == 1:
        return 0
    elif direction == 2:
        return 3
    else:
        return 2


while True:
    if turn > 1000:
        break

    turn += 1
    for i in range(1, k+1):
        now = horseInfo[i]
        x = now.x
        y = now.y
        direction = now.direction
        index = now.index
        if len(boardInfo[x][y]) <= 0:
            continue
        bottom = boardInfo[x][y].popleft()

        if bottom != index:
            boardInfo[x][y].appendleft(bottom)
            continue

        nx = x + dx[direction]
        ny = y + dy[direction]
        boardInfo[x][y].appendleft(bottom)
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if board[nx][ny] == 0:
                white(x, y, nx, ny)
                now.x = nx
                now.y = ny
            elif board[nx][ny] == 1:
                red(x, y, nx, ny)
                now.x = nx
                now.y = ny
            else:
                now.direction = change(direction)
                nx = x + dx[now.direction]
                ny = y + dy[now.direction]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
                    now.direction = change(direction)
                else:
                    if board[nx][ny] == 0:
                        white(x, y, nx, ny)
                        now.x = nx
                        now.y = ny
                    elif board[nx][ny] == 1:
                        now.x = nx
                        now.y = ny
                        red(x, y, nx, ny)

        else:
            now.direction = change(direction)
            nx = x + dx[now.direction]
            ny = y + dy[now.direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
                now.direction = change(direction)
            else:
                if board[nx][ny] == 0:
                    white(x, y, nx, ny)
                    now.x = nx
                    now.y = ny
                elif board[nx][ny] == 1:
                    now.x = nx
                    now.y = ny
                    red(x, y, nx, ny)

        for i in range(1, k+1):
            maxLen = max(maxLen, len(
                boardInfo[horseInfo[i].x][horseInfo[i].y]))

        if maxLen >= 4:
            print(turn)
            exit()

if turn == 1001:
    print(-1)
else:
    print(turn)