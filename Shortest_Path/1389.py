node_num,road_num=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(node_num+1) for _ in range(node_num+1)]


for i in range(road_num):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for k in range(1,node_num+1):
    for a in range(1,node_num+1):
        for b in range(1,node_num+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            graph[b][a]=graph[a][b]

for i in range(node_num+1):
    graph[i][i]=0
            
graph=graph[1:]
results=[]
for row in graph:
    results.append(sum(row)%INF)

print(results.index(min(results))+1)
    