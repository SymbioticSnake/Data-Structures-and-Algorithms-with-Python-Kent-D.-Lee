import copy

def solutionViable(matrix):
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) == 0:
                return False
    
    return True

def solve(matrix):
    reduce(matrix)

    if not solutionViable(matrix):
        return None

    if solutionOK(matrix):
        return matrix

    print("Searching...")

    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) > 1:
                for k in matrix[i][j]:
                    mcopy = copy.deepcopy(matrix)
                    mcopy[i][j] = set([k])

                    result = solve(mcopy)

                    if result != None:
                        return result

    return None