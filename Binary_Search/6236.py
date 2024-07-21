
N,M=map(int,input().split())
moneys=[int(input()) for _ in range(N)]
result=0
start = min(moneys)
end=sum(moneys)

while start <= end:
    count = 1
    budget=(start+end)//2
    current_budget = budget

    for money in moneys:
        if current_budget <money:
            current_budget = budget
            count+=1
        current_budget-=money

    if count <=M and budget >= max(moneys):
        result = budget
        end=budget-1
        
    else:
        start = budget+1
        


print(result)

            
