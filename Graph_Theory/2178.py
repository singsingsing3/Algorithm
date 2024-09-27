from collections import deque

R,C=map(int,input().split())
graph=[list(map(int,(input()))) for _ in range(R)]


def bfs(grpah):
    drow=[-1,1,0,0]
    dcol=[0,0,-1,1] # 상하좌우
    q=deque([(0,0)])
    while q:
        row,col=q.popleft()

        
        for i in range(4):
            next_row,next_col=row+drow[i],col+dcol[i] # 상하좌우 움직이기
            if 0 <= next_row < R and 0 <= next_col < C and graph[next_row][next_col] == 1:
                q.append((next_row,next_col))
                graph[next_row][next_col] = graph[row][col] + 1



    return graph[R-1][C-1]

print(bfs(graph))



