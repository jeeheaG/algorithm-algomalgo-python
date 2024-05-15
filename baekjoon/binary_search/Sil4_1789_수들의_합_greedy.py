# v1 : greedy
#       그리디 / 이진탐색 둘 다로 풀리는 문제
# TS : range 범위 경계값에 걸리는 경우 없는지 생각 잘하기

S = int(input())
answer = 0

add = 0
for i in range(1, S+1) :
    add += i

    #이번 숫자를 더했을 때 주어진 수보다 더 커졌다면, 이번 숫자를 더하지 않고 마지막 더한 수에 남은 수를 합한 수를 마지막으로 더한 경우가 답
    if S < add :
        answer = i-1
        break
    #이번 숫자를 더했을 때 주어진 수와 동일해졌다면, 이번 숫자까지 더한 경우가 답
    elif S == add :
        answer = i
        break

print(answer)