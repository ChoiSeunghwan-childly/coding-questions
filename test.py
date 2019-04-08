answer = True
dic = dict()
arr = [4 , 1, 2, 2, 3 ,5]
arr2 = []

for i in arr:
    if i not in arr2:
        arr2.append(i)
    else:
        answer = False
        break

print(answer)
