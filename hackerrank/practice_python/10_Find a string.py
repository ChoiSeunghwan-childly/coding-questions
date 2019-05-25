def count_substring(string, sub_string):
    count = 0 
    flag = False

    for i in range(len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            flag = True
            for j in range(len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag = False
                    break
            if flag:
                count += 1

    return count            


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)