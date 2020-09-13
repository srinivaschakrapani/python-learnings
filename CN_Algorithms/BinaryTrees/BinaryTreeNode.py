class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None


def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.lc)
    printTree(root.rc)
    return


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


bt = BinaryTreeNode(21)

node1 = BinaryTreeNode(22)

node2 = BinaryTreeNode(23)

node1A = BinaryTreeNode(13)
node1B = BinaryTreeNode(17)

bt.lc = node1
bt.rc = node2

node1.lc = node1A
node1.rc = node1B

# bt.printTree(bt)
root = takeInputTreeV1()
printTreeV2(root)
