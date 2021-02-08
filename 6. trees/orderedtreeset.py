import random


class OrderedTreeSet:
    class BinarySearchTree:
        # This is a Node class that is internal to the BinarySearchTree class.
        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

            def getVal(self):
                return self.val

            def setVal(self, newval):
                self.val = newval

            def getLeft(self):
                return self.left

            def getRight(self):
                return self.right

            def getRightMost(self):
                root = self

                while root.getRight() != None:
                    root = root.getRight()

                return root

            def setLeft(self, newleft):
                self.left = newleft

            def setRight(self, newright):
                self.right = newright

            # This method deserves a little explanation. It does an inorder traversal
            # of the nodes of the tree yielding all the values. In this way, we get
            # the values in ascending order.
            def __iter__(self):
                if self.left != None:
                    for elem in self.left:
                        yield elem

                yield self.val

                if self.right != None:
                    for elem in self.right:
                        yield elem

            def __repr__(self):
                return "OrderedTreeSet.BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"

        # Below are the methods of the BinarySearchTree class.
        def __init__(self, root=None):
            self.root = root

        # def not__contains__(self, item):
        #     return item not in self

        def insert(self, val):
            self.root = OrderedTreeSet.BinarySearchTree.__insert(self.root, val)

        def __insert(root, val):
            if root == None:
                return OrderedTreeSet.BinarySearchTree.Node(val)

            if val < root.getVal():
                root.setLeft(OrderedTreeSet.BinarySearchTree.__insert(root.getLeft(), val))
            else:
                root.setRight(OrderedTreeSet.BinarySearchTree.__insert(root.getRight(), val))

            return root

        def delete(self, val):
            # if val not in self: raise ValueError("Value " + str(val) + " not in BinarySearchTree")
            self.root = OrderedTreeSet.BinarySearchTree.__delete(self.root, val)

        def __delete(root, val):
            # print("Root:", root.getVal())
            if val < root.getVal():
                while root.getLeft() != None:
                    root.setLeft(OrderedTreeSet.BinarySearchTree.__delete(root.getLeft(), val))

            elif val > root.getVal():
                while root.getRight() != None:
                    root.setRight(OrderedTreeSet.BinarySearchTree.__delete(root.getRight(), val))

            if root != None:
                if root.getVal() == val:
                    if root.getLeft() == None and root.getRight() == None:
                        return None

                    elif root.getLeft() != None and root.getRight() == None:
                        return root.getLeft()

                    elif root.getLeft() == None and root.getRight() != None:
                        return root.getRight()
                    
                    elif root.getLeft() != None and root.getRight() != None:
                        left_subtree = root.getLeft()
                        
                        newRootVal = left_subtree.getRightMost().getVal()
                        OrderedTreeSet.BinarySearchTree.__delete(left_subtree, newRootVal)

                        root.setVal(newRootVal)
            
            return root

        def __iter__(self):
            if self.root != None:
                return iter(self.root)
            else:
                return iter([])

        def __str__(self):
            return "BinarySearchTree(" + repr(self.root) + ")"

    def __init__(self, contents=None):
        self.tree = OrderedTreeSet.BinarySearchTree()
        if contents != None:
            # randomize the list
            indices = list(range(len(contents)))
            random.shuffle(indices)

            for i in range(len(contents)):
                self.tree.insert(contents[indices[i]])

            self.numItems = len(contents)
        else:
            self.numItems = 0

    def __str__(self):
        items = []

        for item in self:
            items.append(item)

        return "OrderedTreeSet(" + str(items) + ")"

    def __iter__(self):
        return iter(self.tree)

    # Following are the mutator set methods
    def add(self, item):
        self.tree.insert(item)
        self.numItems += 1

    def remove(self, item):
        if item not in self.tree:
            raise KeyError("Value " + str(item) + " not in OrderedTreeSet")

        self.tree.delete(item)
        self.numItems -= 1

    def discard(self, item):
        try:
            self.tree.delete(item)
            self.numItems -= 1
        except:
            pass

    def pop(self):
        items = []

        for i in self:
            items.append(i)

        item = items[random.randint(0, len(items)-1)]
        self.discard(item)

    def clear(self):
        self.tree.root = None
        self.numItems = 0

    def update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not OrderedTreeSet")

        for item in other:
            if item not in self:
                self.add(item)

    def intersection_update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not OrderedTreeSet")

        for item in self:
            if item not in other:
                self.remove(item)

    def difference_update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not OrderedTreeSet")

        for item in other:
            self.discard(item)

    def symmetric_difference_update(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        tmp = OrderedTreeSet([i for i in self])
        self.difference_update(other)
        self.update(other.difference(tmp))

    # Following are the accessor methods for the HashSet
    def __len__(self):
        return self.numItems

    def __contains__(self, item):
        items = []

        for i in self:
            items.append(i)

        return item in items

    # One extra method for use with the HashMap class. This method is not needed in the
    # HashSet implementation, but it is used by the HashMap implementation.
    def __getitem__(self, item):
        for i in self:
            if i == item:
                return i

        return None

    def not__contains__(self, item):
        return item not in self

    def isdisjoint(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        for item in self:
            if item in other: return False

        return True

    def issubset(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        # USED FOR PROPER SUBSET: if self.numItems <= other.numItems:
        for item in self:
            if item not in other: return False

        return True

    def issuperset(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        # USED FOR PROPER SUPERSET: if self.numItems >= other.numItems:
        for item in other:
            if item not in self: return False

        return True

    def union(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = OrderedTreeSet([i for i in self])
        result.update(other)
        return result

    def intersection(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")
        
        result = OrderedTreeSet([i for i in self])
        result.intersection_update(other)
        return result

    def difference(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = OrderedTreeSet([i for i in self])
        result.difference_update(other)
        return result

    def symmetric_difference(self, other):
        if type(self) != type(other):
            raise TypeError("Type of other object is not HashSet")

        result = OrderedTreeSet([i for i in self])
        result.symmetric_difference_update(other)
        return result

    def copy(self):
        return OrderedTreeSet([i for i in self])

    # Operator Definitions
    def __or__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

    def __sub__(self, other):
        return self.difference(other)

    def __xor__(self, other):
        return self.symmetric_difference(other)

    def __ior__(self, other):
        self.update(other)

    def __iand__(self, other):
        self.intersection_update(other)

    def __ixor(self, other):
        self.symmetric_difference_update(other)

    def __le__(self, other):
        if self.numItems <= other.numItems:
            return self.issubset(other)

        return False

    def __lt__(self, other):
        if self.numItems < other.numItems:
            return self.issubset(other)

        return False

    def __ge__(self, other):
        if self.numItems >= other.numItems:
            return self.issuperset(other)

        return False

    def __gt__(self, other):
        if self.numItems > other.numItems:
            return self.issuperset(other)

        return False

    def __eq__(self, other):
        if self.numItems == other.numItems:
            for item in other:
                if item not in self:
                    return False

            return True

        return False

def main():
    x = OrderedTreeSet([1, 2, 3, 4])
    y = OrderedTreeSet([1, 2, 5, 6])

    x.symmetric_difference_update(y)
    print(x)

if __name__ == "__main__":
    main()
