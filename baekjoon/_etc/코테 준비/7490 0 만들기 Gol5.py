# v1 : eval() 함수 쓰면 풀리는 문제

# fail : eval() 안쓰고 직접 구현 - 25% 틀렸습니다 나오는데 예제는 통과고 테케도 구하기가 어려워서 어디서 틀린건지 모르겠다,,,
# TIP : 파이썬은 문자열 수식을 그대로 넣으면 계산해주는 eval() 함수를 쓰면 금방 풀린다고 함
#       근데 안쓰고 풀어보고 싶었음...ㅎ


'''
[문제 해석]
1~N
+, -, 숫자잇기
결과가 0인 수식 모두만들기

시간제한 : 1초
3 <= N <= 9 
음..구현인가

결과가 0이 되는 모든 수식을 출력


두 자리에 세 경우 모두 넣어보기
1 2 3
123
1+23
1+2+3
1+2-3
1-23
12+3
12-3

세가지 경우 모두 조합해 문자열 탐색 dfs or bfs. eval()로 0인지 계산
'''

import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T) :
    N = int(input())

    ans_T = []

    stack = []
    stack.append((1, ["1"]))

    while stack :
        depth, li = stack.pop()

        if depth == N :
            str_li = "".join(li)
            if eval(str_li.replace(" ", "")) == 0 : # eval() : 수식을 문자열로 넣으면 계산해줌
                ans_T.append(str_li)
            continue

        depth = depth+1
        opers = ["+", "-", " "] # 모든 경우의 수 세가지를 넣어줌
        for oper in opers :
            new_li = li.copy()
            new_li.append(oper)
            new_li.append(str(depth))
            stack.append((depth, new_li))
    
    ans_T.sort()
    ans.append("\n".join(ans_T))

print("\n\n".join(ans))
