import sys
cases = int(sys.stdin.readline().rstrip())
results = []


for case in range(cases):
    result = 0
    index = 0
    N,M=map(int,input().split())
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))
    A.sort()
    B.sort()
    for a in A:
        start = 0
        end = len(B)-1

        while start <= end:
            mid =(start+end) // 2
            if a > B[mid]:
                start = mid + 1

            else:
                end = mid-1

        result += start
    results.append(result)

for i in results:
    print(i)
