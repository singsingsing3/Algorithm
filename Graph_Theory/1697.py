from collections import deque
start,goal=map(int,input().split())
MAX=10**5

def bfs(start,goal):
    q=deque([(start)])
    visited=set() #방문한 노드 처리
    step=0

    while q:
        for i in range(len(q)): # q에 담긴 값들을 우선 step별 처리 -> 내 직관에 더 잘맞는 듯
            now=q.popleft()
            pos=[now-1,now+1,now*2]
            visited.add(now)
            if now == goal:
                return step
            for next in pos:
                if next not in visited and 0 <= next <= MAX :
                    q.append(next)
        step += 1

    return step





print(bfs(start,goal))
