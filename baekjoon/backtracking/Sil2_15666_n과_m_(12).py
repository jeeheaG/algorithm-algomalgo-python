# v1 : 백트래킹

'''
[문제해석]
- N개의 자연수 중 M개 고르기
- 같은 수 여러번 고르기 가능
- 수열은 비내림차순(같거나 오름차순)이어야 함 -> 순서 다른것도 정렬해서 같은걸로 쳐야 함
- 결과는 중복없이, 사전순으로
'''

# import sys
# sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

cur_perm = []

def recur(limit) :
    if len(cur_perm) == M :
        print(*cur_perm)
        return
    
    prev = 0
    for num in nums :
        if num == prev : #중복제거 : 같은 자리에 이미 골랐던 수와 같은 값의 수를 고르는 건 제외
            continue
        if num < limit : #비내림차순
            continue
        
        cur_perm.append(num)
        recur(num)
        cur_perm.pop()
        prev = num

recur(0)