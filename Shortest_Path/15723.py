INF=int(1e9)
n = int(input())
graph=[[INF]*(26)for i in range(26)]

for i in range(26):
    graph[i][i]=1

for i in range(n):
    a,_,b=input().split()
    a=ord(a)-97
    b=ord(b)-97
    graph[a][b]=1

for k in range(26):
    for a in range(26):
        for b in range(26):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

m = int(input())

for i in range(m):
    a,_,b=input().split()
    a=ord(a)-97
    b=ord(b)-97
    print('T' if graph[a][b] < INF  else 'F')





