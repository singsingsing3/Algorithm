N=int(input())
dp_table=[0]*(N+1)
v_table=[0]
for i in range(N):
    v_table.append(int(input()))

for i in range(1,N+1):
    if i==1:
        dp_table[1]=v_table[1]
    elif i==2:
        dp_table[2]=v_table[1]+v_table[2]
    else:
        dp_table[i]=max(dp_table[i-2]+v_table[i],dp_table[i-3]+v_table[i-1]+v_table[i])

print(dp_table[N])