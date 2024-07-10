from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)


for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(graph, visited, start):
    order = 1
    queue = deque([start])
    visited[start] = order
    order += 1

    while queue:
        current = queue.popleft()
        for node in sorted(graph[current]):
            if not visited[node]:
                queue.append(node)
                visited[node] = order
                order += 1

BFS(graph, visited, R)

for i in visited[1:]:
    print(i)
