from collections import deque

N = int(input())
V = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)


for _ in range(V):
    a, b = map(int, input().split())
    graph[a] +=[b]
    graph[b] += [a]

visited[1] = 1
queue = deque([1]) 

while queue:
    current = queue.popleft()
    for node in graph[current]:
        if visited[node] == 0:
            queue.append(node)
            visited[node] = 1

print(sum(visited) - 1)
