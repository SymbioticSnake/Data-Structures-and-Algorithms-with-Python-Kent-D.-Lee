def swap(s):
    if s == "":
        return ""
    
    rem_res = swap(s[2:])

    # print(rem_res)

    two_ch = s[0:2][::-1]
    # print(two_ch)

    result = two_ch + rem_res

    return result

print(swap("abcdefgh"))