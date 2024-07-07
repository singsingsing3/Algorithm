from collections import deque
C, R = map(int,input().split())

graph =[list(map(int, input().split())) for _ in range(R)]

# def DFS(graph,row,col):
#     if row < 0 or row >= R or col < 0 or col >= C:
#         return False
    
#     if graph[row][col] == 1:
#         if row == R - 1 and col == C - 1:
#             return True
#         graph[row][col] = 0
#         drow = [-1,1,0,0]
#         dcol=[0,0,-1,1]
#         for i in range(4):
#            if( DFS(graph,row + drow[i],col + dcol[i])):
#                return True
#     else: return False
    
#     return False
# if DFS(graph,0,0):
#     print('Yes')
# else: print('No')

def BFS(graph):
    if graph[0][0] == 0 or graph[R - 1][C - 1] == 0:
        return False
    queue = deque([(0,0)])
    graph[0][0] = 0

    drow=[1,0]
    dcol=[0,1]

    while queue:
        row, col = queue.popleft()

        
        if row == R -1 and col == C - 1:
            return True
        
        for i in range(2):
            next_row, next_col = row + drow[i], col + dcol[i]

            if 0 <= next_row < R and 0<=next_col < C and graph[next_row][next_col] == 1:
                queue.append((next_row,next_col))
                graph[next_row][next_col] = 0

    return False

if BFS(graph):
    print('Yes')
else:
    print('No')

