# Q : 왜 global 안써도 되지???

'''
대기실 5개 5*5크기
파티션X 없이 거리 2이하 금지

P, 0, X

대기실별 거리두기 지킴 여부
지킴1, 한명이라도 안지킴0 반환

제한시간 : 10초

[구상]
보드 돌면서 P 나오면 좌표 기록.. 아니면 그냥 P 나올때마다 거리 2까지 주변 확인
P 좌표들로 거리 2 이하인 P들 있는지 확인
- 거리 1이면 -> 위반
- 거리 2이면
    - x, y 좌표가 모두 다르면(대각선위치) -> 인접 두 칸 모두 파티션 여부 확인
    - x, y 중 하나가 같으면(일직선위치) -> 둘 사이 칸 하나에 파티션 여부 확인

시간 넉넉
P 나올때마다 주변 확인하는 걸로
구현~
'''

direc_1 = [(0,1), (1,0), (-1,0), (0,-1)]
direc_2 = [(1,1), (-1,1), (1,-1), (-1,-1), (0,2), (2,0), (-2,0), (0,-2)]
P = "P"
X = "X"
PASS = 1
NON_PASS = 0

def isInBoard(i,j) :
    return 0 <= i < 5 and 0 <= j < 5

def isNotX(i) :
    return i != X

def roundPlace(place) :

    # 보드 순회
    for i in range(5) :
        for j in range(5) :
            item = place[i][j]
            if item != P :
                continue

            # P이면 주변 확인
            # 거리 1인 곳
            for di, dj in direc_1 :
                ni = i+di
                nj = j+dj
                if isInBoard(ni,nj) and place[ni][nj] == P :
                    return NON_PASS

            # 거리 2인 곳
            for di, dj in direc_2 :
                ni = i+di
                nj = j+dj
                if isInBoard(ni,nj) and place[ni][nj] == P :
                    # 일직선 위치 - 사이칸에 파티션이 없으면
                    if i == ni :
                        mj = (j+nj)//2
                        if isNotX(place[i][mj]) :
                            return NON_PASS
                    elif j == nj :
                        mi = (i+ni)//2
                        if isNotX(place[mi][j]) :
                            return NON_PASS
                    # 대각선 위치 - 두 곳 다 파티션이 있는 게 아니면
                    else :
                        if isNotX(place[i][nj]) or isNotX(place[ni][j]) :
                            return NON_PASS
    
    return PASS
        

def solution(places):
    
    answer = []
    for place in places :
        answer.append(roundPlace(place))
    
    return answer

ans = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
print(ans)