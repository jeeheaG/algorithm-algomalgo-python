'''
[문제해석]
양수 x, y : 값이 75, 10인 동전 수
앨리스, 밥
앨리스 먼저 시작
항상 합이 115가 되도록 동전 가져가야 함. 못하면 짐


115 = 75 + 10*4
이거밖에 없네??
x 1개, y 4개
y = y // 4 

2 7 -> 2 1 -> 1
4 11 -> 4 2 -> 2
1 1 -> 1 0 -> 0
홀수면 alice, 짝수면 bob이 승
'''
class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """

        y = y // 4

        turn = min(x,y)
        # return "Alice" if turn%2 == 0 else "Bob" #패자 출력
        return "Bob" if turn%2 == 0 else "Alice" #승자 출력

        
        
