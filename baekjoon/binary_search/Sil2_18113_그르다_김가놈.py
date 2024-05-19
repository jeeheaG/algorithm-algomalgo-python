# v1 : 이진탐색
#이름이 왜 이런가 했더니..ㅋㅎㅋㅎ
# TS 1 : 시간초과 -> pypy 로 돌렸더니 돌아가긴 함
# TS 2 : 2% 에서 틀렸습니다 -> 반례 올라와있는 게 몇 없어서 코드 한번 더 검토해보고나서 솔루션 찾아보고 고쳐야 할 듯..?

'''
[문제해석]
- 김밥 양쪽 꼬다리 K씩 자름
    2K보다 짧으면 한쪽만 자름, K이하면 폐기
- 일정한 길이P로 자름
- 김밥이 여러개고, 모든 김밥을 자른 조각 수의 합이 최솟값M 개 이상이도록 자름

답 : 길이P 최대
'''


import sys
input = sys.stdin.readline

N, K, min_cnt = map(int, input().split())
gb_arr = []
for _ in range(N) :
    gb_arr.append(int(input()))


#주어진 길이P로 김밥을 잘라주는 메서드
def cut(P) :
    cnt = 0
    for gb in gb_arr :
        if gb <= K :
            continue
        elif gb < 2*K :
            cnt += (gb - K) // P # 일정??? 남은거 버리기 안됨?
        else : 
            cnt += (gb - 2*K) // P # 일정???
    return cnt


answer = 0
left, right = 0, max(gb_arr)
while left < right :
    mid = (left + right) // 2
    cur_cnt = cut(mid)
    # print(mid, cur_cnt)

    # 최소조각 수min_cnt 이상이어야 함
    if min_cnt < cur_cnt :
        answer = mid
        left = mid + 1
    elif min_cnt == cur_cnt :
        answer = mid
        break
    else :
        right = mid - 1

answer = -1 if answer == 0 else answer
print(answer)
