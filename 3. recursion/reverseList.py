## Normal function: ##
# 
# def revList(lst):
#     accumulator = []

#     for x in lst:
#         accumulator = [x] + accumulator
    
#     return accumulator

# def main():
#     print(revList([1,2,3,4]))

# if __name__ == "__main__":
#     main()

def revList(lst):
    if lst == []:
        return []

    restrev = revList(lst[1:])
    first = lst[0:1]

    result = restrev + first

    return result

def revString(s):
    if s == "":
        return ""

    restrev = revString(s[1:])
    first = s[0:1]

    result = restrev + first

    return result

def revList2(lst):

    def revListHelper(index):
        if index == -1:
            return []
        
        restrev = revListHelper(index-1)
        first = [lst[index]]

        result = first + restrev

        return result
    
    return revListHelper(len(lst)-1)

def main():
    print(revList([1,2,3,4]))
    print(revString("hello"))
    print(revList2([1,2,3,4]))

if __name__ == "__main__":
    main()