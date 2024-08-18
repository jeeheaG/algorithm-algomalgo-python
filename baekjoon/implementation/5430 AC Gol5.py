# v1 : deque, 구현
# TS : ㅇ

'''
[문제 해석]
주어진 문자열에 주어진 연산을 수행한 결과를 출력
- 양쪽에서 제거가 일어나야 하므로 데크deque 사용
- 시간제한이 넉넉하지는 않은 것 같아서 
    뒤집기 연산 시 문자열을 실제로 뒤집지 않고 현재 앞방향을 표시해두고 그에따라 처리하는 방향으로 풀어보겠음
- 시간 제한 : 1초
'''

from collections import deque
import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())) : 
    coms = list(input().strip())
    # print(coms)

    num_cnt = int(input())

    # 빈 숫자배열이 주어지는 경우 처리
    if num_cnt == 0 : 
        nums = deque()
        _ = input()
    else :
        nums = deque(map(int, input().strip("\n[]").split(","))) # TS

    # print(nums)

    isReversed = False
    isError = False

    for com in coms :
        if com == 'R' :
            isReversed = not isReversed
        else : # 'D'인 경우
            if len(nums) <= 0 :
                isError = True
                break

            if isReversed :
                nums.pop()
            else :
                nums.popleft()
    
    # error 가 난 케이스 처리
    if isError :
        ans.append("error")
    else : 
        # 연산이 정상 완료된 경우 마지막 방향에 따라 결과 저장
        if isReversed :
            nums.reverse()
        ans.append("[" + ",".join(map(str, nums)) + "]")

print("\n".join(ans))
