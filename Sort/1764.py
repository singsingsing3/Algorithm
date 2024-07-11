N,M=map(int,input().split())

non_ear = set()
non_eye=set()
for i in range(N):
    non_ear.add(input())
for j in range(M):
    non_eye.add(input())

non_ear_eye=non_ear.intersection(non_eye)
print(len(non_ear_eye))
for name in sorted(list(non_ear_eye)):
    print(name)