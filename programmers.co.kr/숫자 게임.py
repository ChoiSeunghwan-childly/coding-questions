# timeout
# def solution(A, B):
#     answer = 0

#     for i in range(len(A)):
#         valA = max(A)
#         valB = max(B)

#         if valA < valB:
#             A.remove(valA)
#             B.remove(valB)
#             answer += 1
#         else:
#             minB = min(B)
#             A.remove(valA)
#             B.remove(minB)

#     return answer

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    jIndex = 0

    for i in A:
        for j in range(jIndex, len(B)):
            if i < B[j]:
                answer += 1
                B.remove(B[j])
                jIndex = j
                break
    return answer


A = [5, 1, 3, 7]
B = [2, 2, 6, 8]

print(solution(A, B))
