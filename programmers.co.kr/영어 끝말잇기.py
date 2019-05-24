def solution(n, words):
    answer = []
    turn = 0
    tell = []
    flag = False

    tell.append(words.pop(0))
    turn += 1

    for i in range( len(words) ):
        latest = words[i]
        
        if latest in tell:
            flag = True
            break

        if tell[len(tell) -1 ][-1] != latest[0]:
            flag = True
            break
        
        tell.append(latest)
        turn += 1

    if flag:
        player = (turn % n) + 1
        player_turn = int(turn / n) + 1
        answer.append(player)
        answer.append(player_turn)
    else:
        answer.append(0)
        answer.append(0)

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n , words))