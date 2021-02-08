class LinkedQueue:
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next
        
        def getItem(self):
            return self.item

        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
        
        def setNext(self, next):
            self.next = next
    
    def __init__(self, contents=[]):
        self.first = LinkedQueue.__Node(None, None)
        self.last = self.first
        self.numItems = 0
        self.frontIdx = 0

        for e in contents:
            self.enqueue(e)

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty linked queue")

        cursor = self.first.getNext()
        cur_item = cursor.getItem()
        self.frontIdx += 1
        return cur_item
    
    def enqueue(self, item):
        node = LinkedQueue.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1
    
    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty linked queue")
        
        cursor = self.first

        for _ in range(self.frontIdx):
            cursor = cursor.getNext()

        return cursor.getItem()

    def isEmpty(self):
        return self.frontIdx == self.numItems
    
    def clear(self):
        self.first = LinkedQueue.__Node(None, None)
        self.last = self.first
        self.numItems = 0
        self.frontIdx = 0
    
    def __str__(self):
        cursor = self.first
        self.items = []

        for _ in range(self.frontIdx):
            cursor = cursor.getNext()
        
        for _ in range(self.frontIdx, self.numItems):
            cursor = cursor.getNext()
            self.items.append(cursor.getItem())

        return "LinkedQueue(" + str(self.items) + ")"

    def __repr__(self):
        cursor = self.first
        self.items = []

        for _ in range(self.frontIdx):
            cursor = cursor.getNext()
        
        for _ in range(self.frontIdx, self.numItems):
            cursor = cursor.getNext()
            self.items.append(cursor.getItem())

        return "LinkedQueue(" + str(self.items) + ")"

class LinkedStack:
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next
        
        def getItem(self): return self.item

        def getNext(self): return self.next
        
        def setItem(self, item): self.item = item
        
        def setNext(self, next): self.next = next
        
        def __str__(self): return "Node(" + str(self.item) + ")"

        def __repr__(self): return "Node(" + str(self.item) + ")"

    def __init__(self, contents=[]):
        self.first = LinkedStack.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.push(e)
    
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty linked stack")

        cursor = self.first

        for _ in range(self.numItems-1):
            cursor = cursor.getNext()
        
        cur_item = cursor.getNext().getItem()
        self.last = cursor
        cursor.setNext(None)
        
        self.numItems -= 1
        
        return cur_item
    
    def push(self, item):
        node = LinkedStack.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty linked stack")

        cursor = self.first.getNext()

        for _ in range(self.numItems):
            cursor = cursor.getNext()
        
        return cursor.getItem()

    def isEmpty(self):
        return self.numItems == 0

    def __str__(self):
        cursor = self.first
        self.items = []

        for _ in range(self.numItems):
            cursor = cursor.getNext()
            self.items.append(cursor.getItem())

        return "LinkedStack(" + str(self.items) + ")"

    def __repr__(self):
        cursor = self.first
        self.items = []

        for _ in range(self.numItems):
            cursor = cursor.getNext()
            self.items.append(cursor.getItem())

        return "LinkedStack(" + str(self.items) + ")"

def main():
    s = LinkedStack([1, 2, 3, 4]); print(s)
    print("Popped item:", s.pop()); print(s)
    s.push(5); print(s)

    # q = LinkedQueue([1, 2, 3, 4]); print(q)
    # print("Dequeued item:", q.dequeue()); print(q)
    # q.enqueue(5); print(q)
    # q.clear(); print(q)

if __name__ == "__main__": main()