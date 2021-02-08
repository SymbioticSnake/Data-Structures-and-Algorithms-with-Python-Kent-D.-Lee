class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlst = []
        for i in range(self.frontIdx, len(self.items)):
            newlst.append(self.items[i])

        self.items = newlst
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")

        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = []
        self.frontIdx = 0

    def __str__(self):
        return "Queue(" + str([self.items[i] for i in range(self.frontIdx, len(self.items))]) + ")"

    def __repr__(self):
        return "Queue(" + str([self.items[i] for i in range(self.frontIdx, len(self.items))]) + ")"


class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")"

    def postorder(self):
        return self.left.postorder() + " " + self.right.postorder() + " *"


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"

    def postorder(self):
        return self.left.postorder() + " " + self.right.postorder() + " +"


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)

    def postorder(self):
        return str(self.num)


def E(q):
    if q.isEmpty():
        raise ValueError("Invalid Prefix Expression")

    token = q.dequeue()

    # print(token)

    if token == "+":
        # try:
        val_1 = E(q)
        val_2 = E(q)
        return PlusNode(val_1, val_2)
        # except: print("Faulty expression")

    if token == "*":
        # try:
        val_1 = E(q)
        val_2 = E(q)
        return TimesNode(val_1, val_2)
        # except: print("Faulty expression")

    return NumNode(float(token))


def main():
    # x = NumNode(5)
    # y = NumNode(4)
    # p = PlusNode(x, y)
    # t = TimesNode(p, NumNode(6))
    # root = PlusNode(t, NumNode(3))
    # print(root.eval())

    x = input("Please enter a prefix expression: ")

    lst = x.split()
    q = Queue()

    for token in lst:
        q.enqueue(token)

    root = E(q)

    # print(q)

    if len([q.items[i] for i in range(q.frontIdx, len(q.items))]) != 0: print("Malformed expression")
    else:
        print("The infix form is:", root.inorder())
        print("The postfix form is:", root.postorder())
        print("The result is:", root.eval())

if __name__ == "__main__":
    main()
