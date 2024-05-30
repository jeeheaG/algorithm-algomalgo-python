# v3 : bfs - queue(deque) (62040KB, 300ms)

'''
- 연결된 정점 목록
답 : 루트노드를 1번노드로 정했을 때, 2번노드부터 해당 노드의 부모노드 번호를 출력
'''

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
edge = defaultdict(list)

for _ in range(N-1) :
    n1, n2 = map(int, input().split())
    edge[n1].append(n2)
    edge[n2].append(n1)


#bfs
parent_arr = [0]*(N+1)
que = deque()
que.append((1,0))

while que :
    cur, parent = que.popleft()
    for child in edge[cur] :
        if child == parent : #부모노드는 넘어감
            continue
        parent_arr[child] = cur #해당 자식노드의 부모노드로 기록
        que.append((child, cur)) #bfs

#출력
sys.stdout.write('\n'.join(map(str, parent_arr[2:])))