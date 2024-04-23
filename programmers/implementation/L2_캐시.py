# v1
# 구현 문제
# ISSUE : cacheSize 값이 0으로 주어질 경우를 고려못했음. 엣지케이스들 신경 쓸 것

def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    
    #엣지케이스 처리
    if cacheSize == 0 :
        return len(cities)*5

    for city in cities :
        city = city.lower() #대소문자 구분 없앰
        
        #캐시에 있는지 확인, 시간+, 캐시 업데이트
        if city in cache :
            answer += 1
            cache.remove(city)
            cache.append(city)
        else :
            answer += 5
            if cache and cacheSize <= len(cache) :
                cache.pop(0) #맨 첫번째 값 삭제
            cache.append(city)
    
    return answer