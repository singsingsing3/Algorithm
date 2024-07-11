N=int(input())
a =list(map(int,input().split()))
b =list(map(int,input().split()))
S = 0
a.sort()
for i in range(N):
    S += a[i]*sorted(b,reverse=True)[i]

print(S)
