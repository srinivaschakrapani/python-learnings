import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintNodesAtDepthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")

    PrintNodesAtDepthK(root.left, k - 1)  # At each level the depth value is reduced by 1
    PrintNodesAtDepthK(root.right, k - 1)


def PrintNodesAtDepthKV2(root, k, depth=0):
    if root is None:
        return
    if k == depth:
        print(root.data, end=" ")
    # Track the required depth and the current depth , if they are
    # equal,Print
    PrintNodesAtDepthKV2(root.left, k, depth + 1)
    PrintNodesAtDepthKV2(root.right, k, depth + 1)


def buildLevelTree():
    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
root = buildLevelTree()
k = int(input("Enter k:"))
PrintNodesAtDepthK(root, k)
print()
PrintNodesAtDepthKV2(root, k)
# print(PrintNodesAtDepthK(root, k))
