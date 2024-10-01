import sys
N=int(sys.stdin.readline().rstrip())
results=[]
for _ in  range(N):
    M=int(sys.stdin.readline().rstrip())
    applicants=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]
    applicants.sort()
    min=int(1e9)
    cnt=0
    for applicant in applicants:
        if applicant[1] <min:
            min = applicant[1]
            cnt+=1
    results.append(cnt)

for result in results:
    print(result)

