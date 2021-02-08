def strLength(s):
    if s == "":
        return 0

    return 1 + strLength(s[1:])

print(strLength("hello"))