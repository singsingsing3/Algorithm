import sys
N = int(sys.stdin.readline().rstrip())
budget = list(map(int,sys.stdin.readline().split()))
budget_max = int(sys.stdin.readline().rstrip())

start = 1
end = max(budget)

while start <= end:
    middle = (start + end) // 2
    total = 0
    for money in budget:
        if money >= middle:
            total += middle
        else:
            total += money
    
    if total > budget_max:
        end = middle -1
    else:
        result = middle
        start = middle + 1

print(result)
