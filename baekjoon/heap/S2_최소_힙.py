# v1 : 배열을 사용한 최소 힙 구현
#가장 작은 값을 골라내라 -> 최소 힙 연상!

#입력이 0이면 pop, 자연수이면 해당 수 삽입
#배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력

n = int(input())

heap = [0] # 인덱스 1부터 시작하기 위해 0 하나 넣어둠

def heap_pop() :
    if len(heap) == 1 :
        return 0
    else :
        # 루트노드를 말단노드와 swap
        heap[1], heap[-1] = heap[-1], heap[1]
        root = heap.pop()
        min_heapify(1) # 루트노드를 재정렬
        return root


#인덱스 i에 있는 노드를 정렬하는 함수 (최소힙)
def min_heapify(i) :
    size = len(heap)
    idx = 2*i

    #왼쪽노드
    if idx < size and heap[idx] < heap[i] :
        heap[idx], heap[i] = heap[i], heap[idx]
        min_heapify(idx)

    #오른쪽노드
    elif idx+1 < size and heap[idx+1] < heap[i] : # 중복코드 함수화하기
        heap[idx+1], heap[i] = heap[i], heap[idx+1]
        min_heapify(idx+1)
    

def min_heap_insert(num) :
    # print(num, "삽입")
    is_inserted = False
    for i in range(1, len(heap)) :
        if num < heap[i] :
            # 원래 값 킵
            original = heap[i]
            # 현재노드 자리를 새 값으로 변경9
            heap[i] = num
            is_inserted = True

            # 밀려난 원래 값을 새로 삽입
            min_heap_insert(original)

    # 중간에 낄 곳이 없었다면 마지막자리에 추가
    if not is_inserted :
        heap.append(num)


for i in range(n) :
    # 명령값 입력받기(하나씩)
    order = int(input())
    if order == 0 :
        print(heap_pop())
        # print("pop :", heap_pop())
    else :
        min_heap_insert(order)
        # print("삽입 결과 :", heap)


# 테스트
'''
예제 입력
9
0
12345678
1
2
0
0
0
0
32

예제 출력
0
1
2
12345678
0
'''

