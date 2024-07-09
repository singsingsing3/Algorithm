N = int(input())

rope = [int(input()) for _ in range(N)]

rope.sort(reverse=True)
max_weight = 0

for i in range(1, len(rope)+1):
    if i == 1:
        max_weight = rope[0]
    else:
        temp_max_weight = rope[i-1] * i
        if temp_max_weight > max_weight:
            max_weight = temp_max_weight

print(max_weight)