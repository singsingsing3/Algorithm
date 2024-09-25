from collections import deque
import sys

def BFS(graph,start,visited):
    visited[start]=True
    queue=deque([start])
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

N,M=map(int,sys.stdin.readline().rstrip().split())
graph=[[] for i in range(N+1)]
connected_num=0
visited=[False]*(N+1)

for i in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    if not visited[i]:
        BFS(graph,i,visited)
        connected_num +=1

print(connected_num)
