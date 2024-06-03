# v1 : 백트래킹 - dict.fromkeys(리스트)
# TS : 문자열의 정렬은 숫자의 정렬과는 다르다. 숫자 사전순으로 출력 시 문자열인 상태로 정렬하면 안된다..
#       문자열은 각 char 기준으로 정렬해서 두자릿수 이상의 숫자 정렬에서 큰 수가 더 앞에 올 수 있다. 
#       그럼 어떡해?
#       -> 숫자의 경우 숫자인 자료를 미리 정렬해두고 사용하면 됨
#           정렬된 자료에서는, 같은 자리에 사용한 직전값과 비교하면서 만들면 결과를 중복 없이 생성할 수 있음 (이건 재귀일 때만 쓸 수 있는 스킬일까..?)
#       -> 또는 순서 유지하면서 중복 제거하려면 list(dict.fromkeys(리스트)) 사용 가능!

'''
[문제해석]
-답 : N개의 자연수 중 M개를 고른 모든 경우
- 순서 다르면 다름
- 중복 수열 없이 -> 문자열로 만들어서 set에 넣기
- 사전순 출력

구상 : 현재까지의 수열, 사용여부, 숫자 갯수 세기
'''


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() #사전순

perms = [] #순서 유지를 위해 set말고 list사용. 중복제거는 순서가 유지되는 dict.fromkeys()사용할 것
visited = [False]*N
cur_perm = []

#재귀 백트래킹
def recur() :
    #백트래킹 조건 1 : 수열 길이
    if len(cur_perm) == M :
        perms.append(" ".join(map(str, cur_perm))) #공백으로 구분된 문자열로 변환해 저장
        return
    
    for i in range(N) :
        #백트래킹 조건 2 : 이미 사용된 수인지
        if visited[i] :
            continue
        
        visited[i] = True
        cur_perm.append(nums[i])
        recur()
        cur_perm.pop()
        visited[i] = False

#재귀 메서드 시작
recur()

#출력
# TS
print(*list(dict.fromkeys(perms)), sep="\n") #중복제거 후 풀어서 출력