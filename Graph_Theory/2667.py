from  collections import deque
size = int(input())  
graph = [list(map(int, input())) for _ in range(size)]  

block_count=[]

def bfs(graph,row,col):
    count=1
    graph[row][col]=0   
    q=deque([(row,col)])
    drow=[-1,1,0,0]
    dcol=[0,0,-1,1]


    
    while q:
        row,col=q.popleft()
        
        for i in range(4):
            next_row,next_col=row+drow[i],col+dcol[i]
            if 0<= next_row < size and 0 <= next_col < size and graph[next_row][next_col] == 1:
                q.append((next_row,next_col))
                graph[next_row][next_col]=0
                count+=1
    
    return count





for i in range(size):
    for j in range(size):
        if graph[i][j] == 1:
            block_count.append(bfs(graph,i,j))

block_count.sort()
print(len(block_count))
for cnt in block_count:
    print(cnt)

