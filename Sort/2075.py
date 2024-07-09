N = int(input())
arr = []
for i in range(N):
    arr += list(map(int,input().split()))
    arr.sort(reverse= True)
    arr = arr[:N]
    

print(arr[N-1])