from StacksAndQueues import Stack

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def precedence(o):
    # "o" is an operator in string format

    return {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0,
        ")": 0
    }[o]

def cal(r, l, o):
    return {
        "+": l + r,
        "-": l - r,
        "*": l * r,
        "/": l / r
    }[o]

def operate(operator, operator_stack, operand_stack):
    if operator == "(":
        operator_stack.push(operator)
        return
    else:
        while precedence(operator) <= precedence(operator_stack.top()):
            topOp = operator_stack.pop()
            if topOp in ["+", "-", "*", "/"]:
                operand_stack.push(cal(int(operand_stack.pop()), int(operand_stack.pop()), topOp))

            if topOp == "(" and operator == ")": return
        
        operator_stack.push(operator)
        return

def myeval(e):
    exp = e.split()
    oprStk = Stack()
    opdStk = Stack()
    oprStk.push("(")

    for token in exp:
        if isInt(token):
            opdStk.push(token)
        else:
            operate(token, oprStk, opdStk)
        
    operate(")", oprStk, opdStk)
    return opdStk.pop()


def main():
    expr = input("Please enter an infix expression: ")
    result = myeval(expr)
    print("The result of", expr, "is", result, end=".\n")

if __name__ == "__main__": main()
