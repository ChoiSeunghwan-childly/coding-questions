arr = []
peoples = 0
max_peoples = 0

for i in range(4):
    arr.append( list(map(int, input().split())) )

for item in arr:
    peoples = peoples + item[1] - item[0]
    
    if peoples > max_peoples:
        max_peoples = peoples

print(max_peoples)