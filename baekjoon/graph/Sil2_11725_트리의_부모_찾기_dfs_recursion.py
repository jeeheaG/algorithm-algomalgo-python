# v1 : dfs - recursion (71496KB, 336ms)
# TS : dfs 재귀로 구현했는데, 채점에서 Recursion error가 떴다.
#       백준 채점 시 파이썬에서 1000번 이상의 깊이로 재귀호출할 경우 Recursion 에러가 발생하도록 되어있는데, 이 값을 조정할 수 있다.
#       sys.setrecursionlimit(100000) 이렇게
#       이 방식으로 재귀 최댓값을 늘렸을 때, 재귀의 깊이가 채점 서버가 감당할 수 없는 정도로 깊어지면, Segmentation fault가 발생해 런타임 에러 이유로 SegFault를 받게된다고 한다.
#       -> sys.setrecursionlimit(10**9) 로 늘려서 해결. 부하가 있는 것 같으니 다른 방법으로도 풀어봐야겠음

'''
[문제 해석]
- 연결된 정점 목록 주어짐
답 : 루트노드를 1번노드로 정했을 때, 2번노드부터 해당 노드의 부모노드 번호를 출력
'''

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # TS : Recursion error 방지 - 파이썬 재귀호출 깊이 재설정

N = int(input())
edge = defaultdict(list)

for _ in range(N-1) :
    n1, n2 = map(int, input().split())
    edge[n1].append(n2)
    edge[n2].append(n1)


#dfs
parent_arr = [0]*(N+1)

def dfs(cur, parent) :
    for child in edge[cur] :
        if child == parent : #부모노드는 넘어감
            continue
        parent_arr[child] = cur #해당 자식노드의 부모노드로 기록
        dfs(child, cur)

dfs(1,0) #1의 부모노드는 존재하지 않으므로 무의미한 값인 0 넣음

#출력
# print('\n'.join(map(str, parent_arr[2:]))) #아래와 같은 동작
sys.stdout.write('\n'.join(map(str, parent_arr[2:]))) #2번째 노드부터 출력