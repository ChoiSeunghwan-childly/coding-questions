def solution(heights):
    answer = []
    for i in range(len(heights)):
        answer.append(0)
    
    for i in range(1 , len(heights)):
        for j in range( i -1 , -1 , -1 ):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break
    
    return answer