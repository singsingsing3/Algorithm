N = int(input())
coordi = []
for i in range(N):
    coordi.append(list(map(int, input().split())))

coordi.sort(key = lambda x :(x[1],x[0]))
for i in coordi:
    print(f'{i[0]} {i[1]}')