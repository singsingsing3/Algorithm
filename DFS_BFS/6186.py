R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]

def DFS(graph, row, col):
    if row < 0 or row >= R or col < 0 or col >= C or graph[row][col] != '#':
        return False
    
    # 방문 처리
    graph[row][col] = '.'
    
    # 상하좌우 
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]
    
    for i in range(4):
        next_row = row + drow[i]
        next_col = col + dcol[i]
        DFS(graph, next_row, next_col)
    
    return True

count = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            if DFS(graph, i, j):
                count += 1

print(count)
