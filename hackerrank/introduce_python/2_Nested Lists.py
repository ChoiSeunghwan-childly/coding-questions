if __name__ == '__main__':
    students = []
    scores = []
    secNum = 0

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])

    scores.sort()
    
    for i in range(1, len(scores)):
        if scores[0] < scores[i]:
            secNum = scores[i]
            break

    names = []
    for item in students:
        if item[1] == secNum:
            names.append(item[0])
    names.sort()
    
    for _ in names:
        print(_)