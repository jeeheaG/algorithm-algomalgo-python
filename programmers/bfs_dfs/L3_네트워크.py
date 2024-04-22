# v1 : bfs
# bfs 내 풀이로 도전 - 솔루션보면서 몇가지 조건 고쳐서 solve
# ISSUE 1 : 현재 노드의 간선을 탐색하는 for문에서 range함수의 범위를 range(node, n) 로 하면 될 줄 알았는데, 그래프 탐색 시 현재 노드에 연결된 간선을 모두 확인해야 하므로 range(n)으로 해야 함
# ISSUE 2 : ISSUE 1 수정으로 인해 간선을 큐에 넣기 전에 방문여부를 확인해줘야 함! 아니면 무한루프 돎

from collections import deque

def solution(n, computers):
    answer = 0
    
    que = deque()
    visited = [False]*n
    
    # 모든 노드를 순서대로 돌면서
    for i in range(n) :
        if not visited[i] :
            que.append(i)
            visited[i] = True
            answer += 1 #새로운 네트워크 시작

            while que :
                node = que.popleft()
                
                # 현재 노드의 간선 탐색
                for j in range(n) :
                    # 현재 노드와 간선으로 연결된 노드이고 아직 방문 전이라면
                    if computers[node][j] == 1 and visited[j] == False :
                        que.append(j)
                        visited[j] = True
    
    return answer


# 테스트
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) #2