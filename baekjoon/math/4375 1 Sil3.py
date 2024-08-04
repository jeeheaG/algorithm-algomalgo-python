# v1 : 그냥 짬
# 이건 문자열 합연산으로 짬

'''
[문제 해석]
정수 n이 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수 최소값을 찾아라
- n은 2와 5로 나누어 떨어지지 않음
- 시간제한 : 1초
- 출력 : 찾은 수의 자릿수 출력

3 -> 3*37 = 111 -> 3
7 -> 111111 -> 6
9901 -> 1이 12개인 수 -> 12

어떻게 찾지
다 해본다고 생각하면 1 11 111 하나씩 다 나눠보면 됨. 젤먼저 나머지 없는게 답
이거래 ㄱㄱ~
'''


import sys

coms = list(map(int, sys.stdin.readlines()))

# print(coms)

ans = []
for com in coms :
    num = "1"
    while int(num) % com != 0 :
        num += "1" # 이 문자열 합연산이 굉장히 오래걸리는 듯

    ans.append(str(len(num)))

print('\n'.join(ans))