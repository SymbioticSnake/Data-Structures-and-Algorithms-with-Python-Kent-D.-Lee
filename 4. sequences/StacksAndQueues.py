class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
            
        topIdx = len(self.items) - 1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
        
    def push(self, item):
        self.items.append(item)
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")

        topIdx = len(self.items)-1
        return self.items[topIdx]
    
    def isEmpty(self):
        return len(self.items) == 0

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

def main():
    ## Stack Code ##
    #
    # s = Stack()
    # lst = list(range(10))
    # lst2 = []

    # for k in lst:
    #     s.push(k)

    # if s.top() == 9: print("Test 1 Passed")
    # else: print("Test 1 Failed")

    # while not s.isEmpty():
    #     lst2.append(s.pop())

    # lst2.reverse()

    # if lst2 != lst: print("Test 2 Failed")
    # else: print("Test 2 Passed")

    # try:
    #     s.pop()
    #     print("Test 3 Failed")
    # except RuntimeError: print("Test 3 Passed")
    # except: print("Test 3 Failed")

    # try:
    #     s.top()
    #     print("Test 4 Failed")
    # except RuntimeError: print("Test 4 Passed")
    # except: print("Test 4 Failed")

    ## Queue Code ##

    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k)
    
    if q.front() == 0: print("Test 1 Passed")
    else: print("Test 1 Failed")

    while not q.isEmpty(): lst2.append(q.dequeue())

    if lst2 != lst: print("Test 2 Failed")
    else: print("Test 2 Passed")

    for k in lst: q.enqueue(k)

    lst2 = []

    while not q.isEmpty():
        lst2.append(q.dequeue())

    if lst2 != lst: print("Test 3 Failed")
    else: print("Test 3 Passed")

    try:
        q.dequeue()
        print("Test 4 Failed")
    except RuntimeError: print("Test 4 Passed")
    except: print("Test 4 Failed")

    try:
        q.front()
        print("Test 5 Failed")

    except RuntimeError: print("Test 5 Passed")
    except: print("Test 5 Failed")

if __name__ == "__main__": main()