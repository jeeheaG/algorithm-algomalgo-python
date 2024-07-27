# v1 : ?? 모르겟는디

'''
[문제해석]
- S -> E 최단거리
- 이동 방법
    1. 현위치에서 +1 or -1
    2. 현위치의 텔레포트 정거장에 연결된 정거장으로 이동
'''

N, M = map(int, input().split())
S, E = map(int, input().split())

port = [tuple(map(int, input().split())) for _ in range(M)]

