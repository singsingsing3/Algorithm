length=int(input())
people=list(map(int,input().split()))
people.sort()
time=0

for i in range(len(people)):
    time+=sum(people[:i+1])

print(time)