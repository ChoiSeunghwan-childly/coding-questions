def solution(progresses, speeds):
    answer = []
    completed_count = 0
    
    while True:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        
        for i in range(completed_count , len(progresses)):
            if progresses[i] >= 100:
                completed_count += 1
                count += 1
            else:
                break
        
        if count > 0:
            answer.append(count)
            
        if completed_count >= len(progresses):
            break
    
    return answer