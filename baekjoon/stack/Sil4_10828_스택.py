# v1 : 그냥 배열써서 구현함... 너무 간단한데 이게 맞나 더 날것으로 만들어야 하나
# 스택을 구현해랴

'''
[문제 해석]
시간제한 0.5s
- 아래 기능들 구현
    - push, pop, top, size, empty
    - 비어있는데 pop, top하면 -1
    - empty는 비어있으면 1, 아니면 0
'''

import sys
input = sys.stdin.readline

N = int(input())
com_arr = [list(input().split()) for _ in range(N)] # 2차원 배열. 명령어 한줄씩, 공백으로 구분된 리스트로 받음

stack = []

def push(x) :
    stack.append(x)

def pop() :
    return stack.pop() if stack else -1

def top() :
    return stack[-1] if stack else -1

def size() :
    return len(stack)

def empty() :
    return 0 if stack else 1 #요소가 있으면 0 반환

for com in com_arr :
    action = com[0]
    if action == "push" : push(com[1])
    elif action == "pop" : print(pop())
    elif action == "top" : print(top())
    elif action == "size" : print(size())
    elif action == "empty" : print(empty())


