import sys
input=sys.stdin.readline #sys기반 input선언 
test_case=int(input())
for i in range(test_case):
    n=int(input())
    count=0
    min=1e9
    scores=[list(map(int,input().split())) for _ in range(n)] #2차원 배열 입력 받기
    scores.sort(key=lambda x:x[0]) # 0 column기준으로 정렬
    for score in scores: #2차원배열에서 1행씩 빼오기
        if score[1] < min:
            count +=1
            min=score[1]

    print(count)

