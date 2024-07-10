N = int(input())
houses = list(map(int, input().split()))

houses.sort()

locate = houses[(N - 1) // 2]

print(locate)

