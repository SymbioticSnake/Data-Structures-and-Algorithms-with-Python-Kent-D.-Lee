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
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"

    # Below are the methods of the BinarySearchTree class.
    def __init__(self, root=None):
        self.root = root

    def __contains__(self, item):
        valList = []

        for val in self:
            valList.append(val)

        return item in valList

    # def not__contains__(self, item):
    #     return item not in self

    def insert(self, val):
        self.root = BinarySearchTree.__insert(self.root, val)

    def __insert(root, val):
        if root == None:
            return BinarySearchTree.Node(val)

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(), val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(), val))

        return root

    def delete(self, val):
        # if val not in self: raise ValueError("Value " + str(val) + " not in BinarySearchTree")
        self.root = BinarySearchTree.__delete(self.root, val)

    def __delete(root, val):
        # print("Root:", root.getVal())
        if val < root.getVal():
            while root.getLeft() != None:
                root.setLeft(BinarySearchTree.__delete(root.getLeft(), val))

        elif val > root.getVal():
            while root.getRight() != None:
                root.setRight(BinarySearchTree.__delete(root.getRight(), val))

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
                    BinarySearchTree.__delete(left_subtree, newRootVal)

                    root.setVal(newRootVal)
        
        return root

    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"


def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    # for x in tree:
    #     print(x)

    s2 = input("Enter a value to delete: ")
    tree.delete(float(s2))

    # print(tree.root)

    for x in tree: print(x)

if __name__ == "__main__":
    main()
