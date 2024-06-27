# BJ class 2

import sys
input = sys.stdin.readline

N = int(input())
word = list(set(input().strip() for _ in range(N))) #중복제거

for i in range(len(word)) :
    w = word[i]
    word[i] = (len(w), w) #(문자열 길이, 문자열) 로 저장 - 사전순 정렬 시 길이순으로 먼저 정렬되고 그다음 문자열 사전순으로 정렬됨

print(*[w for _, w in sorted(word)]) #정렬 후 문자열만 가진 리스트로 만들어 풀어서 출력