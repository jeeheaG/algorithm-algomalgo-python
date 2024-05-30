# v2 : dfs (permutation)
# dfs 재귀로도 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/43165


def solution(numbers, target):
    answer = 0

    end_depth = len(numbers)
    
    def dfs(num, depth) :
        if depth == end_depth :
            if num == target :
                nonlocal answer #현재 함수 내의 지역변수가 아닌 변수를 사용하겠다는 뜻
                answer += 1
        else : 
            dfs(num + numbers[depth], depth+1)
            dfs(num - numbers[depth], depth+1)
    
    dfs(0, 0)

    return answer

# 테스트
print(solution([4, 1, 2, 1], 4))

