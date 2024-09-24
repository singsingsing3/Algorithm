import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i]=s
            dfs(i)

dfs(1)

for i in range(2,n+1):
    print(visited[i])