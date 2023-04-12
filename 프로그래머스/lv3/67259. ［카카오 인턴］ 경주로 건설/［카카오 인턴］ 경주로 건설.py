from collections import deque
import copy
import sys

d = [[0,1],[1,0],[-1,0],[0,-1]]

class Car : pass
    
def find(board) :
    return ;

def solution(board):
    answer = 0
    
    dq = deque()
    
    cost = [[[1e9 for _ in range(len(board))] for _ in range(len(board))] for k in range(4)]
    
    cost[0][0][0] = 0
    cost[1][0][0] = 0
    cost[2][0][0] = 0
    cost[3][0][0] = 0

    
    for i in range (4) :
        car = Car()
        car.x = 0
        car.y = 0
        car.corner = 0
        car.straight = 0
        car.direc = i
        dq.append(car)
    while dq :
        now = dq.popleft()
        x = now.x
        y = now.y
        
        #방향을 이동하는데 이전방향이랑 지금 이동하려는 방향이 다르면 체크
        for i in range(4) :
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            
            if nx >=0 and nx < len(board) and ny >= 0 and ny < len(board) :
                if board[nx][ny] != 1 :
                    newNow = Car()
                    newNow.x = nx
                    newNow.y = ny
                    newNow.corner = now.corner
                    newNow.straight = now.straight
                    newNow.direc = i
                    
                    if newNow.direc != now.direc :
                        newNow.corner +=1
                    newNow.straight +=1
                    
                    total = newNow.straight * 100  +  newNow.corner * 500
                    
                    if cost[newNow.direc][nx][ny] > total :
                        cost[newNow.direc][nx][ny] = total
                        dq.append(newNow)        
    return min([cost[0][-1][-1],cost[1][-1][-1],cost[2][-1][-1],cost[3][-1][-1]])