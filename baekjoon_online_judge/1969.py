# 1969 (그리드) DNA

from collections import Counter

N, M = map(int, input().split())
dnas = []
s = ''

for _ in range(N):
    dnas.append(input().rstrip())

for i in range(M):
    word_list = []
    for j in range(N):
        word_list.append(dnas[j][i])
    
    c = Counter(word_list)
    max_ch = ''
    count = 0
    for ch in c.keys():
        if c[ch] >= count:
            
            if c[ch] == count:
                if ch < max_ch:
                    max_ch = ch
                    count = c[ch]
            else:
                max_ch =ch
                count = c[ch]

    s += max_ch

count = 0

for dna in dnas:
    for i in range(len(dna)):
        if dna[i] != s[i]:
            count += 1

print(s)
print(count)