n=int(input())
INF = int(1e9)
graph=[[INF]*(n+1) for i in range(n+1)]


for i in range(1,n):
    m = int(input())
    arr=list(map(int,input().split()))
    for j in arr:
        graph[i][j] = 1

notCycled = True

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(n+1):
    if graph[i][i] < INF and graph[1][i] < INF:
        notCycled=False
        break

if notCycled:
    print('NO CYCLE')
else:
    print('CYCLE')
