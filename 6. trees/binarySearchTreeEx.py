from binarySearchTrees import BinarySearchTree

tree = BinarySearchTree()
mainTrig = False

while not mainTrig:
    choice = input("Make a choice...\n1. Insert into tree.\n2. Delete from tree.\n3. Lookup value.\nChoice? ")
    
    insert = "x"
    del_value = "x"
    lookup = "x"

    if choice == "1":
        while True:
            insert = input("\tInsert? ")
            if insert.split() == []: break
            else: tree.insert(float(insert))
    
    elif choice == "2":
        del_value = input("\tValue? ")
        try:
            tree.delete(float(del_value))
            print(float(del_value), "has been removed from the tree.")
        except:
            print("Invalid value (either input is invalid or value is not in the tree)")

    elif choice == "3":
        lookup = input("\tValue? ")
        if float(lookup) in tree: print(float(lookup), "is in the tree.")
        else: print(float(lookup), "is not in the tree.")
    
    elif choice.split() == []: break

    else: print("Invalid choice.")