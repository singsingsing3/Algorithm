N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def DFS(graph, row, col):
    if row >= N or row < 0 or col < 0 or col >= N or graph[row][col] == 0:
        return False
    
    if graph[row][col] == -1:
        return True
    
    drow = [-1, 1, 0, 0]  # 상하좌우
    dcol = [0, 0, -1, 1]
    
    step = graph[row][col]
    graph[row][col] = 0  # 방문 처리

    for i in range(4):
        new_row = row + drow[i] * step
        new_col = col + dcol[i] * step
        if DFS(graph, new_row, new_col):
            return True
    
    return False

if DFS(graph, 0, 0):
    print('HaruHaru')
else:
    print('Hing')
