import heapq

INF = int(1e9)
N, D = map(int,input().split())

graph=[[] for _ in range(D+1)]
distance=[INF]*(D+1)

for i in range(N):
    a,b,c=map(int,input().split())
    if b <= D:
        graph[a].append((b,c))

for i in range(D):
    graph[i].append((i+1,1))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(0)
print(distance[D])


