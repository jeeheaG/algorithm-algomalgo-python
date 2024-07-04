# BJ CLASS 2

'''
- 시간제한 0.25초
시간제한때문에 반복문 없이 수식으로 해결해야 하는데 수식정리 머리가 안굴러가서 애먹은 문제..^.^
math.ceil() 대신 그냥 /나누기연산 후 int()함수 적용한 결과와 같은지 비교해서 소수점유무를 알아내 처리해도 올림과 같은 효과를 낼 수 있다.

'''
import math
A, B, V = map(int, input().split())

day = A-B
print(math.ceil((V-A)/day)+1)