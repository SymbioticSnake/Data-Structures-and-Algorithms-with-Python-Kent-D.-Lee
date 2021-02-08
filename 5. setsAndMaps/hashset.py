from random import randint

class HashSet:
    class __Placeholder:
        def __init__(self): pass
        def __eq__(self, other): return False
        def __str__(self): return "__Placeholder()"
        def __repr__(self): return "__Placeholder()"

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.numItems = 0

        for item in contents: self.add(item)

    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            if items[idx] == item:
                # item already in set
                return False
            
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx
            
            idx = (idx + 1) % len(items)

        if loc < 0: loc = idx

        items[loc] = item

        return True
    
    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)
        
        return newList

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)

            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None] * 2 * len(self.items))
    
    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                
                if items[nextIdx] == None: items[idx] = None
                else: items[idx] = HashSet.__Placeholder()

                return True
            
            idx = (idx + 1) % len(items)
        
        return False

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)

            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))

        else: raise KeyError("Item not in HashSet")

    def discard(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)

            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))

    def __contains__(self, item):
        idx = hash(item) % len(self.items)

        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return self.items[idx]

            idx = (idx+1) % len(self.items)

        return None

    def update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        for item in other.items:
            if item != None and type(item) != HashSet.__Placeholder \
                and item not in self.items: self.add(item)

    def intersection_update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        for item in self.items:
            if item != None and type(item) != HashSet.__Placeholder \
                and item not in other.items: self.discard(item)

    def difference_update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        for item in other:
            self.discard(item)

    def symmetric_difference_update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        tmp = HashSet(self)
        self.difference_update(other)
        self.update(other.difference(tmp))

    def pop(self):
        itemList = []

        for item in self.items:
            if item != None and type(item) != HashSet.__Placeholder:
                itemList.append(item)
        
        val = itemList[randint(0, len(itemList)-1)]

        self.discard(val)

        return val

    def clear(self):
        self.items = [None] * 10
        self.numItems = 0

    def isdisjoint(self, other):
        for item in self.items:
            if item != None and type(item) != HashSet.__Placeholder \
                and item in other.items: return False

        return True

    def issubset(self, other):
        if self.numItems <= other.numItems:
            for item in self.items:
                if item != None and type(item) != HashSet.__Placeholder \
                    and item not in other.items: return False

        return True

    def issuperset(self, other):
        if self.numItems >= other.numItems:
            for item in other.items:
                if item != None and type(item) != HashSet.__Placeholder \
                    and item not in self.items: return False

        return True

    def union(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = HashSet(self)
        result.update(other)
        return result

    def intersection(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = HashSet(self)
        result.intersection_update(other)
        return result

    def difference(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = HashSet(self)
        result.difference_update(other)
        return result

    def symmetric_difference(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = HashSet(self)
        result.symmetric_difference_update(other)
        return result

    def copy(self):
        return HashSet(self)

    def __str__(self):
        items = []

        for item in self.items:
            if item != None and type(item) != HashSet.__Placeholder: items.append(item)
            
        return "HashSet(" + str(items) + ")"

    def __repr__(self):
        return self.__str__()

def main():
    x = HashSet([1, 2, 3, 4])
    y = HashSet([1, 2, 3])

    print(x.issubset(y))

if __name__ == "__main__": main()