import sys
num,goal = map(int,sys.stdin.readline().split())
line = [int(sys.stdin.readline().rstrip()) for _ in range(num)]
result = 0

start = 1
end = max(line)
while start <= end:
    mid = (start + end) // 2
    total = 0


    for x in line:
        if x >= mid:
            total += x//mid
    
    if total < goal:
        end = mid -1
    else:
        start = mid + 1
        result = mid

print(result)
