# BJ CLASS 2

'''
펠린드롬수인지 아닌지 출력
'''

import sys
input = sys.stdin.readline

answer = []
while True :
    n = input().strip()
    if n == '0' : break
    
    is_pelin = True
    l, r = 0, -1
    while l <= len(n)//2 :
        if n[l] != n[r] :
            is_pelin = False
            break
        l += 1
        r -= 1
    
    answer.append("yes" if is_pelin else "no")

print('\n'.join(answer))