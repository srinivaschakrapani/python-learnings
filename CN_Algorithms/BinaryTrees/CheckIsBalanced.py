# What is balanced Tree ?
# For each node in a tree , that node's
# left and right sub tree should not have
# height difference of more than One
# Time complexity:
# O(n*h) where h is height of tree
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


def heightOfTree(root):
    if root is None:
        return 0
    return 1 + heightOfTree(root.lc) + heightOfTree(root.rc)


def checkIsBalanced(root):
    if root is None:
        return True
    left_ht = heightOfTree(root.lc)
    right_ht = heightOfTree(root.rc)

    if left_ht - right_ht > 1 or right_ht - left_ht > 1:
        return False
    return checkIsBalanced(root.lc) and checkIsBalanced(root.rc)

def checkIsBalancedV2(root):
    if root is None:
        return 0, True
    lh, lftBal = checkIsBalancedV2(root.lc)
    rh, rtBal = checkIsBalancedV2(root.rc)
    h = 1 + max(lh, rh)

    if lftBal and rtBal:
        return h, True
    else:
        return h, False

    if left_ht - right_ht > 1 or right_ht - left_ht > 1:
        return False
    return checkIsBalanced(root.lc) and checkIsBalanced(root.rc)

# bt.printTree(bt)
root = takeInputTreeV1()
print("Before")
printTreeV2(root)
print(checkIsBalanced(root))
print(checkIsBalancedV2(root))

'''
1
2
4
6
-1
-1
-1
-1
3
-1
5
-1
-1
'''