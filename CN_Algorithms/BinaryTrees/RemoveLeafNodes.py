class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None

def printTreeV2(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.lc is not None:
        print("L", root.lc.data, end=",")
    if root.rc is not None:
        print("R", root.rc.data, end=" ")
    print()
    printTreeV2(root.lc)
    printTreeV2(root.rc)
    return


def takeInputTreeV1():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = takeInputTreeV1()
    rightTree = takeInputTreeV1()
    root.lc = leftTree
    root.rc = rightTree
    return root

def removeLeafNodes(root):
    if root is None:
        return root
    if root.lc is None and root.rc is None:
        return None
    a = removeLeafNodes(root.lc)
    b = removeLeafNodes(root.rc)
    root.lc = a
    root.rc = b
    return root
# bt = BinaryTreeNode(21)
#
# node1 = BinaryTreeNode(22)
#
# node2 = BinaryTreeNode(23)
#
# node1A = BinaryTreeNode(13)
# node1B = BinaryTreeNode(17)
#
# bt.lc = node1
# bt.rc = node2
#
# node1.lc = node1A
# node1.rc = node1B

# bt.printTree(bt)
root = takeInputTreeV1()
print("Before")
printTreeV2(root)
removeLeafNodes(root)
print("After")
printTreeV2(root)

