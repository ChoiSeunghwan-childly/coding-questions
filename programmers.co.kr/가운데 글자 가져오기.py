def solution(s):
    s_len = len(s)
    len_div = int(s_len/2)
    if s_len % 2 == 0:
        return s[len_div-1] + s[len_div]
    else:
        return s[len_div]
    