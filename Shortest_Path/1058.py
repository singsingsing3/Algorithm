n = int(input())
graph=[[0]*n for i in range(n)]
friend=[list(input()) for i in range(n)]

for k in range (n):
    for a in range(n):
        for b in range(n):
            if a==b:
                continue
            if friend[a][b]=='Y' or (friend[a][k]=='Y' and friend[k][b]=='Y'):
                graph[a][b]=1

temp=0
for row in graph:
    temp=max(temp,sum(row))

print(temp)

            


