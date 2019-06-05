def solution(arrangement):
    answer = 0
    bar = 0
    
    for i in range(len(arrangement)):
        if arrangement[i] == '(' and arrangement[i+1] != ')':
            bar += 1
            answer += 1
        elif arrangement[i] == ')':
            if arrangement[i-1] =='(': #cut
                answer += bar
            else:
                bar -= 1
                
    return answer