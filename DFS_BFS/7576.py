from collections import deque
col, row = map(int, input().split())
graph=[list(map(int,input().split())) for _ in range(row)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs():
    queue = deque()
    for i in range(row):
        for j in range(col):
            if graph[i][j]==1:
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<row and 0<=ny<col and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
def check():
    result=0
    for i in graph:
        if 0 in i: 
            return -1
        result=max(result,max(i))
    return result-1
bfs()
print(check())
