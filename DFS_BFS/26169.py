graph = []
apple_count = 0
move_count = 0

graph=[list(map(int,input().split())) for _ in range(5)]

current_row, current_col = map(int,input().split())

# 1 사과 0 통로 -1 장애물
def DFS(graph, row, col, move_count, apple_count):
    move_count += 1
    if row < 0 or row > 4 or col < 0 or col > 4:  # 범위 밖
        return False
    if move_count > 4:  # 3번 초과
        return False
    if graph[row][col] == -1:  # 장애물
        return False

    if graph[row][col] == 1:  # 사과인 경우
        apple_count += 1
        if apple_count == 2:
            return True

    original_value = graph[row][col]
    graph[row][col] = -1  # 방문 표시

    if (DFS(graph, row - 1, col, move_count, apple_count) or
        DFS(graph, row + 1, col, move_count, apple_count) or
        DFS(graph, row, col - 1, move_count, apple_count) or
        DFS(graph, row, col + 1, move_count, apple_count)):
        return True

    graph[row][col] = original_value  # 상태 복구
    return False


if DFS(graph, current_row, current_col, move_count, apple_count):
    print('1')
else:
    print('0')
