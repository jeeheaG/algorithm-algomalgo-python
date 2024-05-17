# v3 : 이진탐색..의 느낌을 더 살려서! (44ms)
# TS : 이분탐색 시 다음 범위는 현재 중간값을 포함하지 않는 범위로 설정해줄 것!
# TIP : 갱신하면서 탐색 : 정확한 정답인지 조건을 확인하지 않아도, 갱신하면서 이진탐색을 다 돌고 나면 최종적으로 정답만 남게 되어있음

S = int(input())
answer = 0

start, end = 1, S #이진탐색의 left, right인덱스
while start <= end :
    #이진탐색
    mid = (start + end) // 2
    add = mid*(mid+1) // 2 #1~n까지의 합 = n(n+1)/2

    if S < add :
        end = mid - 1 # TS
    elif S == add :
        answer = mid
        break
    elif add < S :
        start = mid + 1
        answer = mid #TIP : 갱신하면서 탐색

    
print(answer)