# 1120 - 문자열 (그리디)

s1, s2 = input().split()
offset = 0

hit_count = 0

for i in range(0, len(s2) - len(s1) + 1 ):
    temp_count = 0
    for j in range(len(s1)):
        if s1[j] == s2[i+j]:
            temp_count += 1
    if temp_count > hit_count:
        hit_count = temp_count
        offset = i

for i in range(offset -1 , -1 , -1):
    s1 = s2[i] + s1
    hit_count += 1

for _ in range(len(s2) - len(s1)):
    s1 = s1 + s2[len(s1)]
    hit_count += 1

print(len(s1) - hit_count) 

    
    