from collections import Counter

def solution(participant, completion):
    c = Counter(participant) - Counter(completion)
    return list(c)[0]