# ing : 다익이라면.. 부분최적구조로 생각.. 해당 노드까지의 최적경로가 아니라 intentsity최대값을 구해놓으면 되려나? 시뮬해보기
#모든 봉우리에 대해 다익스트라를 하는데, 산봉우리거나 출입구이면 탐색 안함으로 풀어보자

#[문제해석]
#n개 = 출/쉼/산봉. 등산로로 이동
#등산코스. 쉼/산봉 = 휴식, 휴식없이 intensity
#출-산봉-출, 1산봉, 쉼터 껴서 intensity최소. 같은 출입구로 올 것
#**intensity최소가 여러개라면 산봉번호가 낮은 경로로 반환



def solution(n, paths, gates, summits):
    answer = []
    return answer