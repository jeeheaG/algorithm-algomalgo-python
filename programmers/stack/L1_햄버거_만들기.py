# v1 : 스택

def solution(ingredient):
    stack = []
    cnt = 0
    
    for ing in ingredient :
        stack.append(ing)
        if 4 <= len(stack) :
            if stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1 :
                cnt += 1
                for _ in range(4) : stack.pop()
    
    return cnt