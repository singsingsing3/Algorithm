N=int(input())
times=[list(map(int,input().split())) for _ in range(N)]
times.sort(key=lambda x:(x[1],x[0])) 
print(times)
end=0
cnt=0
for time in times:
    if time[0]>=end:
        end=time[1]
        cnt+=1
print(cnt)
