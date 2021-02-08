from StacksAndQueues import Queue

def charAt(s, i):
    if len(s) - 1 < i:
        return " "
    
    return s[i]

def radixSort(list_of_strings):
    mainQueue = Queue()
    longest = 0
    
    for i in list_of_strings:
        mainQueue.enqueue(i)
        
        if longest < len(i):
            longest = len(i)
            cur_idx = len(i)

    cur_idx -= 1

    queueList = []
    for _ in range(256):
        queueList.append(Queue())

    print(mainQueue)

    while cur_idx >= 0:
        for _ in range(len(mainQueue.items)):
            s = mainQueue.dequeue()
            # print(s)
            ch = charAt(s, cur_idx)
            # print(ch)
            q_val = ord(ch)
            # print(q_val)
            queueList[q_val].enqueue(s)

        mainQueue.clear()
        print(mainQueue)

        for i in range(len(queueList)):
            q = queueList[i]

            print("Queue w/ Index " + str(i) + ": ", q)

        for i in range(len(queueList)):
            q = queueList[i]

            print("Length of Queue w/ Index " + str(i) + ": ", q.frontIdx)

            while q.frontIdx < len(q.items):
                print("Length of Queue w/ Index " + str(i) + ": ", q.frontIdx)
                s = q.dequeue()
                mainQueue.enqueue(s)
                print(mainQueue)

        for i in range(len(queueList)):
            q = queueList[i]; q.clear()

        cur_idx -= 1

    # print(queueList)
    print(mainQueue)

example = ["bat", "farm", "barn", "car", "hat", "cat"]
# example = ["bat"]

radixSort(example)

# print(queueList)