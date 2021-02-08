import hashset


class HashMap:
    class __KVPair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            return self.key == other.key

        def getKey(self): return self.key
        def getValue(self): return self.value
        def __hash__(self): return hash(self.key)
        def __str__(self): return (str(self.key) + ": " + str(self.value))
        def __repr__(self): return self.__str__()

    def __init__(self): self.hSet = hashset.HashSet()
    def __len__(self): return len(self.hSet)
    def __contains__(self, item): return HashMap.__KVPair(
        item, None) in self.hSet

    def not__contains__(self, item): return item not in self.hSet

    def __setitem__(self, key, value): self.hSet.add(
        HashMap.__KVPair(key, value))

    def __getitem__(self, key):
        if HashMap.__KVPair(key, None) in self.hSet:
            val = self.hSet[HashMap.__KVPair(key, None)].getValue()
            return val

        raise KeyError("Key " + str(key) + " not in HashMap")

    def __iter__(self):
        for x in self.hSet:
            yield x.getKey()

    def get(self, key, default=None):
        if HashMap.__KVPair(key, None) in self.hSet:
            val = self.hSet[HashMap.__KVPair(key, None)].getValue()
            return val

        return default

    def __delitem__(self, key):
        if HashMap.__KVPair(key, None) in self.hSet:
            self.hSet.discard(HashMap.__KVPair(key, None))

        else:
            raise KeyError("Key" + str(key) + " not in HashMap")

    def items(self):
        kvL = []

        for k in self:
            kvL.append(tuple([k, self[k]]))

        return kvL

    def keys(self):
        kL = []

        for k in self:
            kL.append(k)

        return kL

    def values(self):
        vL = []

        for k in self:
            vL.append(self[k])

        return vL

    def pop(self, key):
        if HashMap.__KVPair(key, None) in self.hSet:
            value = self[key]
            self.hSet.discard(HashMap.__KVPair(key, None))
            return value

        else:
            raise KeyError("Key" + str(key) + " not in HashMap")

    def popitem(self):
        kvpair = self.hSet.pop()
        return tuple([kvpair.getKey(), kvpair.getValue()])

    def setdefault(self, key, default=None):
        self.hSet.add(HashMap.__KVPair(key, default))

    def update(self, other):
        if type(self) != type(other):
            raise TypeError("Argument is " +
                            str(type(other)) + ", not HashMap")

        for k in other:
            self.hSet.add(HashMap.__KVPair(k, other[k]))

    def clear(self):
        self.hSet.clear()

    def copy(self):
        return HashMap(self)

    def __str__(self):
        kvS = "{"
        kvL = []

        for item in self.hSet:
            if type(item) == HashMap.__KVPair:
                kvL.append(item)

        for item in kvL:
            if item != kvL[-1]:
                kvS += (str(item) + ", ")
            else:
                kvS += str(item)

        kvS += "}"

        return kvS

    def __repr__(self):
        return self.__str__()


def main():
    x = HashMap()
    x[1] = 2
    x[5] = 9

    y = HashMap()
    y[9] = 10
    y[4] = 8

    print(x)
    x.update(y)
    print(x)

    x.clear()
    print(x)


if __name__ == "__main__":
    main()
