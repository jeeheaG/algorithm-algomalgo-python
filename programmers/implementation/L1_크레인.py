# v1
# 햄버거 만들기 문제에서 쓴 방법을 사용해보자
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    
    basket = []
    board_height = len(board)
    
    for move in moves :
        idx = move-1
        for i in range(board_height) :
            cur_board = board[i][idx]
            #현재 열에 가장 위에 있는 인형을 basket으로 옮김
            if cur_board != 0 :
                basket.append(cur_board)
                board[i][idx] = 0
                
                #같은 인형 2개면 삭제, 갯수+
                if 2 <= len(basket) and basket[-1] == basket[-2] :
                    #마지막 두개 삭제
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))