# v1 : stack, greedy?

'''
[문제 해석]
주어진 숫자에서 숫자 K개를 지웠을 때 얻을 수 있는 가장 큰 수 구하기

고려해야할 조건
- 자릿수 (앞으로 갈수록 큰 숫자가 자리하도록)
- 그 숫자 자체

앞에서부터 그 다음자리가 현재자리보다 크면 현재자리 삭제
-> 아이디어는 맞음! 구현에 스택을 떠올릴 것..~
'''

import sys
input = sys.stdin.readline

stack = []
N, K = map(int, input().split())

nums = tuple(map(int, input().strip()))
cnt = 0
for num in nums :
    #앞에서부터 숫자를 돌면서 바로 앞 숫자가 현재숫자보다 커질때까지 앞 숫자를 지운다. K개까지만 지운다
    while stack and stack[-1] < num and cnt < K:
        stack.pop()
        cnt += 1
    stack.append(num) #앞 숫자가 더 커졌거나 K를 다 지웠으면 append

#K개를 다 못지웠다면 이미 앞으로 갈수록 더 큰 숫자라는 뜻이므로, 뒤쪽을 잘라냄
print(''.join(map(str, stack[:N-K])))