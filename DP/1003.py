N = int(input())
case = [int(input())for _ in range(N)]
dp_table=[[0]*2 for _ in range(41)]
dp_table[0][0]=1
dp_table[1][1]=1

for i in range(2,41):
    dp_table[i][0] = dp_table[i-2][0] + dp_table[i-1][0]
    dp_table[i][1] = dp_table[i-2][1] + dp_table[i-1][1]

for i in case:
    print(f'{dp_table[i][0]} {dp_table[i][1]}')



