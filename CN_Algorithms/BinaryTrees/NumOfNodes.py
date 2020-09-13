class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None

def NumNodes(root):
    if root is None:
        return 0
    lc = NumNodes(root.lc)
    rc = NumNodes(root.rc)
    return 1 + lc + rc

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

root = takeInputTreeV1()
k = NumNodes(root)
print(k)
