n = int(input())
road = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if road[a][k] == 1 and road[k][b] == 1:
                road[a][b] = 1

for row in road:
    print(*row)
