import sys

N = int(sys.stdin.readline().rstrip())  
solutions = list(map(int, sys.stdin.readline().split()))  


start = 0
end = len(solutions) - 1
closest_sum = float('inf')  
result = (0, 0)  

while start < end:
    curr_sum = solutions[start] + solutions[end]

 
    if abs(curr_sum) < abs(closest_sum):
        closest_sum = curr_sum
        result = (solutions[start], solutions[end])

   
    if curr_sum > 0:
        end -= 1
    elif curr_sum < 0:
        start += 1
    else:
        
        result = (solutions[start], solutions[end])
        break

print(result[0], result[1])
