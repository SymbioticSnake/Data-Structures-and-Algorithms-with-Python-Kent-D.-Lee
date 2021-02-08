def getGroups(matrix):
    ## Creating groups list ##
    groups = []

    ## Adding shallow copies of each row in the matrix ##
    for row in matrix:
        groups.append(list(row))

    # for row in groups:
    #     print("Row #" + str(groups.index(row)) + ":", row, end="\n\n")

    ## Appending each set into its respective column and adding it ##
    ## into the groups list - each set is the same as the original ##

    c = 0

    while c <= 8:
        newLst = []

        for row in matrix:
            # print("Row #" + str(groups.index(row)) + ":", row, end="\n\n")
            newLst.append(row[c])

        # print(newLst, end="\n\n")
        groups.append(newLst)

        c += 1

    # for group in groups:
    #     print(group, end="\n\n")

    ## Adding squares to group list ##

    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s6 = []
    s7 = []
    s8 = []
    s9 = []

    for row in matrix:
        if matrix.index(row) < 3:
            s1.append(row[0])
            s1.append(row[1])
            s1.append(row[2])
            s2.append(row[3])
            s2.append(row[4])
            s2.append(row[5])
            s3.append(row[6])
            s3.append(row[7])
            s3.append(row[8])

        elif 3 <= matrix.index(row) < 6:
            s4.append(row[0])
            s4.append(row[1])
            s4.append(row[2])
            s5.append(row[3])
            s5.append(row[4])
            s5.append(row[5])
            s6.append(row[6])
            s6.append(row[7])
            s6.append(row[8])

        elif 6 <= matrix.index(row) < 9:
            s7.append(row[0])
            s7.append(row[1])
            s7.append(row[2])
            s8.append(row[3])
            s8.append(row[4])
            s8.append(row[5])
            s9.append(row[6])
            s9.append(row[7])
            s9.append(row[8])

    groups.append(s1)
    groups.append(s2)
    groups.append(s3)
    groups.append(s4)
    groups.append(s5)
    groups.append(s6)
    groups.append(s7)
    groups.append(s8)
    groups.append(s9)

    # for group in groups:
    #     print(group, end="\n\n")

    return groups


def reduceGroups(groups):
    for group in groups:
        set_dict = {}
        single_items = []

        for s in group:
            if str(s) not in set_dict: set_dict[str(s)] = 1
            else: set_dict[str(s)] += 1

        for s in group:

            for s2 in group:
                if len(s2) == set_dict[str(s2)] and s != s2:

                    for item in s2: s.remove(item)

        for s in group:
            if len(s) == 1:
                for item in s:
                    single_items.append(item)

        for s in group:
            if len(s) != 1:
                for item in single_items:
                    try:
                        s.remove(item)
                    except:
                        pass

    # for group in groups:
    #     for s in group:
    #         if len(s) == dup_count[str(s)]: # and s != set([i + 1 for i in range(9)]):

    #             for s2 in group:
    #                 print(s2)
    #                 if s2 != s:
    #                     for item in s: s2.remove(item)

    # return True


# def reduce(matrix):
#     changed = True
#     groups = getGroups(matrix)

#     reduceGroups(groups)

#     # while changed:
#     #     changed = reduceGroups(groups)

def main():
    file = open("D:\Tito\Documents\Tito\Documents\Python\Textbook Work\Textbook Exercises\Algorithms Textbook Work\\5. setsAndMaps\Sudoku.txt")

    matrix = []
    # print(matrix)

    for r in range(9):
        line = file.readline()
        row = line.split()
        newLst = []

        # print("Row #" + str(r) +":", row)

        for c in range(9):
            # print("Row #" + str(r) + " | " + "Col #" + str(c) + ":", row[c])

            if row[c] == "x":
                newLst.append(set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
            else:
                newLst.append(set([int(row[c])]))

        matrix.append(newLst)

    groups = getGroups(matrix)
    reduceGroups(groups)
    reduceGroups(groups)
    reduceGroups(groups)

    # for group in groups:
    #     print(group)

    for row in matrix: print(row)

    # for r in range(9):
    #     for c in range(9):
    #         print("[" + str(r) + "][" + str(c) + "]:", matrix[r][c])

if __name__ == "__main__": main()