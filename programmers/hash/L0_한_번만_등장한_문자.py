# v1 : 딕셔너리 사용해 구현
# Q. 이게 해시문제라는데 왜지?

# TS : 딕셔너리의 인덱스와 값을 함께 가져오는 법(items), 문자열을 사전순 정렬하는 법(join) 등 기본적인 파이썬 문법 챙기기
# TIP : 파이썬 문자열에는 문자열 내에서 주어진 요소가 몇개 포함되어있는지 세주는 함수 count가 존재한다..! 이걸로도 풀이 가능

from collections import defaultdict

def solution(s):
    answer = ''
    
    cnt = defaultdict(int)
    for letter in s :
        cnt[letter] += 1
    
    for key, val in cnt.items() :
        if val == 1 :
            answer += key
    
    answer = ''.join(sorted(answer))
    
    return answer