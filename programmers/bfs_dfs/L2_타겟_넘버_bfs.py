# type : bfs
# 큐를 사용한 bfs로 풀이 가능

from collections import deque

def solution(numbers, target):
    answer = 0
    
    que = deque()
    end_cnt = len(numbers)
    que.append((numbers[0],1))
    que.append((-1*numbers[0],1))
    
    while que :
        num, cnt = que.popleft()
        if cnt == end_cnt :
            if num == target :
                answer +=1
        else :
            que.append((num + numbers[cnt], cnt+1))
            que.append((num - numbers[cnt], cnt+1))
        
    return answer

# 테스트
print(solution([4, 1, 2, 1], 4))