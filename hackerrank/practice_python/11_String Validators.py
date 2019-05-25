if __name__ == '__main__':
    s = input()  
    flag1, flag2, flag3, flag4, flag5 = [ False for _ in range(5) ]

    for i in range(len(s)):
        if s[i].isalnum():
            flag1 = True
        if s[i].isalpha():
            flag2 = True
        if s[i].isdigit():
            flag3 = True
        if s[i].islower():
            flag4 = True
        if s[i].isupper():
            flag5 = True

    print(flag1, flag2, flag3, flag4, flag5, sep='\n', end='\n')