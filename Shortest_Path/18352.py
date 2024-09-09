# #Floyd-Warshal -> memory issue! failed!
# import sys
# node_num, road_num, goal, start = map(int,sys.stdin.readline().rstrip().split())
# INF=int(1e9)
# result=[]

# graph=[[INF]*(node_num+1)for _ in range(node_num+1)]

# for i in range(node_num+1):
#         graph[i][i]=0

# for i in range(road_num):
#     s,e=map(int,sys.stdin.readline().rstrip().split())
#     graph[s][e]=1

# for k in range(node_num+1):
#     for a in range(node_num+1):
#         for b in range(node_num+1):
#             graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# for i in range(node_num+1):
#     if graph[start][i] == goal:
#         result.append(i)

# if result:
#     for i in sorted(result):
#         print(i)
# else:
#     print(-1)

###Dijkstra
import heapq
import sys
INF =int(1e9)
node_num, road_num, goal, start = map(int,sys.stdin.readline().rstrip().split())

graph=[[] for i in range(node_num+1)]
distance_table =[INF]*(node_num+1)

for i in range(road_num):
    s,e=map(int,sys.stdin.readline().rstrip().split())
    graph[s].append((e,1))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance_table[start]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance_table[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance_table[i[0]]:
                distance_table[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

result=[]
dijkstra(start)

for i in range(node_num+1):
    if distance_table[i] == goal:
        result.append(i)

if result:
    for i in result:
        print(i)

else:
    print(-1)




