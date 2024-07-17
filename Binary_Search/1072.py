total_game,win_game = map(int,input().split())
win_rate = win_game  * 100 // total_game #Z

start = 1
end = total_game
result = -1


while start <= end:
    mid = (start + end) // 2
    temp = (win_game + mid)* 100 // (total_game + mid) 
    if temp > win_rate:
        result = mid
        end = mid -1
    else: 
        start = mid + 1

if temp >= win_rate:
    print(result)

else: print(-1)
    
        

