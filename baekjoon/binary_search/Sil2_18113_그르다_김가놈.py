# v1 : 이진탐색
#이름이 왜 이런가 했더니..ㅋㅎㅋㅎ
# TS 1 : 시간초과 -> 이 풀이는 pypy 로 돌려야 풀 수 있다고 함
# TS 2 : 2% 에서 틀렸습니다 -> mid로 나눗셈 연산을 해야해서 mid가 0이면 안됨. left=1로 시작하고 left<=right 로 같은 경우 포함시켜주기
# TS 4 : 80%쯤에서 틀렸습니다 -> 이진탐색 if문에서 이번값==목표값 인 경우에도 최적의 정답이 아닐 수 있으므로 바로 break로 탈출하면 안됨. 범위 조절해서 이어서 탐색해줘야 함..
#           (아마도 김밥 남은거 버리고 꼬다리 자르고 뭐 그래서 그런듯...wow)

'''
[문제해석]
- 김밥 양쪽 꼬다리 K씩 자름
    2K보다 짧으면 한쪽만 자름, K이하면 폐기
- 일정한 길이P로 잘린 것만 카운트함. 남은 건 버려짐
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
            cnt += (gb - K) // P
        else : 
            cnt += (gb - 2*K) // P
    return cnt


answer = 0
left, right = 1, max(gb_arr) # TS 3
while left <= right :
    mid = (left + right) // 2
    cur_cnt = cut(mid)

    # 최소조각 수min_cnt 이상이어야 함
    if min_cnt <= cur_cnt : # TS 4 : min_cnt == cur_cnt 인 경우에도 break하면 안되고 계속 탐색해줘야 함
        answer = mid
        left = mid + 1
    else :
        right = mid - 1

answer = -1 if answer == 0 else answer
print(answer)
