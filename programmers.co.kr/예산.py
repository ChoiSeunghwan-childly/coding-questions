def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)




# def solution(d, budget):
#     answer = 0
#     cost = 1
    
#     while budget >= cost and len(d) != 0:
#         minIndex = d.index(min(d))            
#         cost = d.pop(minIndex)
        
#         if(budget >= cost):
#             budget -= cost
#             answer += 1

#     return answer



# d = [1, 3, 5, 11]
# budget = 9
# print(solution(d, budget))