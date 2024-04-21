# fail : 아직 푸는 중..
# bfs 내 풀이로 도전 - 테스트케이스 2개만 통과하고 나머지 다 실패

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
                node = que.pop()
                
                # 간선 테이블의 우측상단 삼각형(i>j인) 부분만 탐색
                for j in range(node+1, n) :
                    print(j)
                    # 현재 노드와 간선으로 연결된 노드라면
                    if computers[node][j] == 1 :
                        que.append(j)
                        visited[j] = True
    
    return answer


# 테스트
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) #2