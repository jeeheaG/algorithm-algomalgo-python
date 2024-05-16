# v2 : 이진탐색 (48ms)
# TS : sum(range()) 는 시간이 꽤 드는 함수다. 
#       -> sum(1~n)는 n(n+1)/2 로 대체하여 사용하자!

S = int(input())
answer = 0

start, end = 1, S
while True :
    #이진탐색
    mid = (start + end) // 2
    # add = sum(range(mid+1)) # 0부터 mid까지 더함 -> TS : 시간초과..! (시간제한 2초)
    add = mid*(mid+1) // 2 #1~n까지의 합 = n(n+1)/2

    #합이 S보다 크면 앞쪽 탐색
    if S < add :
        end = mid
        continue
    #합이 같으면 바로 답
    elif S == add :
        answer = mid
        break
    #합이 S보다 작으면 이게 최적인지 체크 후 아닐 시 뒷쪽 탐색
    elif add < S :
        #지금이 최적인가?
        if S < add + mid+1 :
            answer = mid
            break
        else :
            start = mid
            continue

    
print(answer)