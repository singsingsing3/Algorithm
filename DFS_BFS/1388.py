row, col = map(int, input().split())
house = []
for i in range(row):
    house.append(list(input()))

def dfs(x,y):


    if house[x][y] == '-':
        house[x][y] = 1
        right = y + 1
        if  right < col and house[x][right] == '-':
            dfs(x,right)
        



    
    if house[x][y] =='|':
        house[x][y] = 1
        down = x + 1
        if down < row and house[down][y] == '|':
            dfs(down,y)


count = 0
for i in range(row):
    for j in range(col):
        if house[i][j] =='-' or house[i][j] =='|':
            dfs(i,j)
            count += 1

print(count)
