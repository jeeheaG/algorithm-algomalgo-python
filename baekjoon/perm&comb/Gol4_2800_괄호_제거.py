# v1 : 조합, 스택
# TS : 입력조건, 출력조건 명시되어있는 것들 꼼꼼히 보고 처리해주기!!

'''
[문제 해석]
- 주어진 식의 괄호쌍 포함/미포함 모든 조합 출력
- 괄호는 쌍으로만 포함/미포함 시킴
- 출력은 사전순으로, 중복 없이

구상
- 스택으로 괄호쌍 개수 세고, 괄호 위치 저장해둠
- 각 괄호 포함/미포함 조합들을 itertools.combinaions()로 조합 생성함. 괄호개수가 4개면 4P0 + 4P1 + 4P2 + 4P3 가 총 조합수가 됨(모두 포함하는 경우인 4P4는 제외)
- 해당 조합에 해당하는 괄호만 포함시켜 출력
'''

from itertools import combinations
import sys
input = sys.stdin.readline

com = input().strip() #입력 엔터 제거

#괄호쌍 별로 위치 기록해두기
idx_arr = []
stack = []
for i in range(len(com)) :
    letter = com[i]
    if letter == "(" : #여는 괄호는 임시저장소에 쌓아둠
        stack.append(["(", i])
    elif letter == ")" : #닫는 괄호를 만났을 때, 마지막 열린 괄호와 위치 기록
        # if bag and bag[-1][0] == "(" : #이 조건 확인안해도 되긴 함. 입력에 이상한 괄호는 없어서
        idx_arr.append([stack[-1][1], i])
        stack.pop()

# print(idx_arr)
p_cnt = len(idx_arr) #괄호쌍 개수

#제거할 경우의 수대로 조합 생성
answer_set = set()
p_li = range(p_cnt)
for i in range(1, p_cnt+1) :
    for combi in list(combinations(p_li, i)) :
        #삭제할 괄호들의 인덱스번호 모음 생성
        remove_idx = []
        for p in combi :
            remove_idx += idx_arr[p] 
        # print(remove_idx)

        #삭제할 괄호들의 인덱스번호들을 포함시키지 않은 문자열 생성
        answer = ""
        for j in range(len(com)) : 
            if j in remove_idx :
                continue
            else : 
                answer += com[j]
        answer_set.add(answer)
        
#사전순 출력, 중복없이
answer_arr = list(answer_set)
answer_arr.sort()
for answer in answer_arr :
    print(answer)
