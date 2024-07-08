N = int(input())
member = []
for i in range(N):
    data = input().split()
    member.append((int(data[0]),data[1]))

member.sort(key= lambda x : x[0])

for info in member:
    print(f'{info[0]} {info[1]}')
