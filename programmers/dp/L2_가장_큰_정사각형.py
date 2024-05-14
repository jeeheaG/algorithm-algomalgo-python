# v1 : dp 최적부분구조 반복계산. bottom-up(반복문)
#으아 이론 연결몰라몰라 일단 아는 솔루션을 풀어내보자!

def solution(board):
    
    h, w = len(board), len(board[0])
    
    for i in range(h) :
        for j in range(w) :
            
            if board[i][j] == 0 :
                continue
            
            if i==0 or j==0 :
                continue
            
            #주변 정사각형 한 변 값의 최솟갑 + 1 이 현위치에서의 정사각형 한 변 최댓값
            board[i][j] = min(min(board[i-1][j], board[i][j-1]), board[i-1][j-1]) + 1
    
    #최댓값 구하기
    max_len = 0
    for boxes in board :
        for box in boxes :
            if max_len < box :
                max_len = box
            
    return max_len**2 #한 변을 넓이로 반환