# v1 : 

'''
[문제 해셕]
- 0~N 까지의 수 중 K개를 더한 값이 N이 되는 경우의 수
- 순서가 다르면 다른 것
- 중복 허용(한개의 수 여러번 사용 가능)
- 1 <= N, K <= 200
- 답 : 경우의 수를 1,000,000,000으로 나눈 나머지
- 시간제한 : 2초

6 4
0 0 0 0 < 6
6 0 0 0 = 6

1 1 1 1 < 6
2 1 1 1 < 6
2 2 1 1 = 6


6 0 0 0 
5 1 0 0 
4 1 1 0 
4 2 0 0 
3 1 1 1 

0 0 0 6
0 0 1 5
0 1 1 4
0 0 2 4
1 1 1 3

그냥 브루트포스.. dfs 백트래킹?
0~N다 더해보기 재귀로

'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
def dfs(cur, cnt) :
    # if K < cnt or N < cur : 
    #     return
        
    if cnt == K and cur == N :
        global answer
        answer += 1
        return
    
    new_cnt = cnt+1
    if K < new_cnt :
        return 
    
    for i in range(N+1) :
        new_cur = cur+i
        if N < new_cur :
            break
        dfs(new_cur, new_cnt)

dfs(0, 0)
print(answer)