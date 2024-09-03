N=int(input())
cost_table=[list(map(int,input().split())) for _ in range(N)]
dp_table=[[0]*3 for _ in range(N)]
for row in range(N):
    for col in range(3):
        if row==0:
            dp_table[row][col]=cost_table[row][col]
        else:
            if col==0:
                dp_table[row][col]=min(dp_table[row-1][1],dp_table[row-1][2])+cost_table[row][col]
            elif col==1:
                dp_table[row][col]=min(dp_table[row-1][0],dp_table[row-1][2])+cost_table[row][col]
            else:
                dp_table[row][col]=min(dp_table[row-1][0],dp_table[row-1][1])+cost_table[row][col]

print(min(dp_table[N-1]))