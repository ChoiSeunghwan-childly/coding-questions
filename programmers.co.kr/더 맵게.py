import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
        
    while len(heap) > 1:
        val1 = heapq.heappop(heap)
        val2 = heapq.heappop(heap)
        
        if val1 >= K:
            return answer
        answer += 1
        sco = val1 + (val2 * 2)
        heapq.heappush(heap, sco)
    
    if heap[0] >= K:
        return answer
    return -1