def solution(answers):
    answer = []

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p_arr = [0, 0, 0]

    for i in range(len(answers)):
        if arr1[i%5] == answers[i]:
            p_arr[0] += 1
        if arr2[i%8] == answers[i]:
            p_arr[1] += 1
        if arr3[i%10] == answers[i]:
            p_arr[2] += 1

    max_index = p_arr.index(max(p_arr))
    for i in range(len(p_arr)):
        if p_arr[i] == p_arr[max_index]:
            answer.append(i+1)

    return answer