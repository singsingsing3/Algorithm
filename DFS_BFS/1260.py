from collections import deque



N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]

visited_BFS = [0] * (N+1)
sequence_BFS = []

for i in range(M):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

visited_BFS[V] = 1 #V부터 방문
sequence_BFS.append(V)

queue = deque([V])




while queue:
    current = queue.popleft()
    for neighbor in sorted(graph[current]):
        if visited_BFS[neighbor] == 0:
            queue.append(neighbor)
            visited_BFS[neighbor] = 1
            sequence_BFS.append(neighbor)

visited_DFS = [0]*(N+1)
sequence_DFS = []

visited_DFS[V] = 1
sequence_DFS.append(V)

def DFS(graph, v, visited, sequence):
    visited[v] = 1
    
    for i in sorted(graph[v]):
        if visited[i] == 0:
            sequence.append(i)
            DFS(graph,i,visited,sequence)

DFS(graph, V, visited_DFS, sequence_DFS)

print(*sequence_DFS)
print(*sequence_BFS)


