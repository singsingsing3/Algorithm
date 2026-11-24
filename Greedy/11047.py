N,K=map(int,input().split())
coins=[int(input()) for _ in range(N)]
count=0
coins.sort(reverse=True)
for coin in coins:
    if K-coin >=0:
        count+=K//coin
        K=K%coin
    if K==0:
        break

print(count)
    