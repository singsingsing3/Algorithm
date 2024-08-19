dp_table =[0]*11
dp_table[1]=1
dp_table[2]=2
dp_table[3]=4
for i in range(4,11):
    dp_table[i]=dp_table[i-1]+dp_table[i-2]+dp_table[i-3]



case=[]
N=int(input())
for i in range(N):
    case.append(int(input()))

for i in case:
    print(dp_table[i])
