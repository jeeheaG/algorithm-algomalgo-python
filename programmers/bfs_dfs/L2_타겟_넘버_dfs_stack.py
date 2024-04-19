# v2 : dfs (stack)
# dfs stack으로도 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/43165


def solution(numbers, target):
    answer = 0

    stack = []
    end_depth = len(numbers)
    stack.append((0, 0))

    while stack :
        num, depth = stack.pop()

        if depth == end_depth :
            if num == target :
                answer += 1
        else :
            stack.append((num + numbers[depth], depth+1))
            stack.append((num - numbers[depth], depth+1))

    return answer

# 테스트
print(solution([4, 1, 2, 1], 4))