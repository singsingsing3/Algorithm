N=int(input())
count=0

while N >=3:
    if N%5==0:
        count+=N//5
        N=N%5
        break
    else:
        count+=1
        N=N-3

if N!=0:
    print(-1)
else:
    print(count)



    

"""
5로 먼저 채워보고 안되면 3으로 한번 채우기
다시 5로 채우고... 반복...
마지막 남은게 3미만으로 남으면 5,3 조합으로 채울 수 없으므로 -1 출력
"""