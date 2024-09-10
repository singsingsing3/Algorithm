# Dijkstra practice
import heapq
import sys
INF=int(1e9)

#노드 수, 간선 수, 시작노드 입력받기
INF=int(1e9)
node_num,road_num,start_node=map(int,sys.stdin.readline().rstrip().split())

#graph 초기화, 거리 table 생성
graph=[[] for i in range(node_num+1)]
distance=[INF]*(node_num+1)

# 모든 간선 정보 입력받기 (시작, 끝, 가중치)
for i in range(road_num):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append((b,c))

# Dijkstra 함수 생성
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush((cost,i[0]))

#Floyd-Warshal
INF=int(1e9)
# 노드의 개수, 간선의 개수 입력받기
node_num,road_num=map(int,sys.stdin.readline().rstrip().split())

# graph 초기화
graph=[[INF]*(node_num+1) for i in range(node_num+1)]

# 자기자신 -> 자기자신 거리는 0으로 초기화
for i in range(node_num+1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for i in range(road_num):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    graph[a][b]=c

# 플로이드 와샬 알고리즘 수행
for k in range(1,node_num+1):
    for a in range(1,node_num+1):
        for b in range(1,node_num+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 그래프 출력


