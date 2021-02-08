def select(seq, start):
    minIndex = start

    for j in range(start+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j
    
    return minIndex

def selSort(seq):
    for i in range(len(seq)-1):
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp

x = [5, 8, 2, 6, 9, 1, 0, 7]
selSort(x)
print(x)

def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    while i < mid and j < stop:
        # If the <seq> value located at index <i> is less than
        # the <seq> value located at index <j>, then the former
        # is appended to the function's list; otherwise, the
        # latter is appended
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
            print(lst)
        else:
            lst.append(seq[j])
            j += 1
            print(lst)
    
    while i < mid:
        # While there are still leftover <seq> values from indexes <i>
        # to <mid>, add all of the <seq> values to the end of <lst>.
        lst.append(seq[i])
        i += 1

    # while j < stop:
    #     lst.append(seq[j])
    #     j += 1

    for i in range(len(lst)):
        seq[start+i] = lst[i]

def mergeSortRecursively(seq, start, stop):
    if start >= stop-1:
        return
    
    mid = (start + stop) // 2

    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))

y = [1, 9, 0, 4, 2, 5]
mergeSort(y)
print(y)

import random

def partition(seq, start, stop):
    # pivotIndex comes from the start location in the list
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start + 1
    j = stop - 1

    while i <= j:
        # while i <= j and seq[i] <= pivot:
        while i <= j and not pivot < seq[i]:
            i += 1
        # while i <= j and seq[j] > pivot:
        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i += 1
            j -= 1
    
    seq[pivotIndex] = seq[j]
    seq[j] = pivot

    return j

def quicksortRecursively(seq, start, stop):
    if start >= stop - 1:
        return

    pivotIndex = partition(seq, start, stop)

    quicksortRecursively(seq, start, pivotIndex)
    quicksortRecursively(seq, pivotIndex+1, stop)

def quicksort(seq):
    for i in range(len(seq)):
        j = random.randint(0, len(seq)-1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp
    
    quicksortRecursively(seq, 0, len(seq))