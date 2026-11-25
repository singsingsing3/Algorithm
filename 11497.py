import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
diffs=[]
for _ in range(n):
    num=int(input())
    woods=list(map(int,input().split()))
    woods.sort()
    woods_deque=deque(woods)

    dq=deque([woods_deque.pop()])
    while woods_deque:
        dq.append(woods_deque.pop())
        if not woods_deque:
            break
        dq.appendleft(woods_deque.pop())
    dq=list(dq)
    diff=0
    for i in range(num):
        if i==num-1:
            diff=max(diff,abs(dq[i]-dq[0]),abs(dq[i]-dq[i-1]))
        else: diff=max(diff,abs(dq[i]-dq[i+1]),abs(dq[i]-dq[i-1]))
    diffs.append(diff)

for i in diffs:
    print(i)



"""
<정석풀이>
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  woods = sorted(map(int, input().split()))

  # 양 끝 원소끼리 인접할 수 있으므로 초기값은 (최대 - 두 번째 큰 값) 또는 (두 번째 작은 값 - 최소)
  ans = max(woods[1] - woods[0], woods[-1] - woods[-2])

  # 정렬된 배열에서 두 칸씩 떨어진 원소들의 차이를 확인
  for i in range(n - 2):
    ans = max(ans, woods[i + 2] - woods[i])

  print(ans)

직접 정려해보면서 패턴파악 -> 2칸씩 비교하면 되는 것을 확인
"""