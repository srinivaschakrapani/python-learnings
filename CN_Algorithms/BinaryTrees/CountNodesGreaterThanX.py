import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodesGreaterThanX(root, x):
    # Given a Binary Tree and an integer x, find and return the count of nodes
    # which are having data greater than x.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return 0
    left_side = root.left
    right_side = root.right
    if x < root.data:
        return 1 + countNodesGreaterThanX(left_side, x) + countNodesGreaterThanX(right_side, x)
    else:
        return countNodesGreaterThanX(left_side, x) + countNodesGreaterThanX(right_side, x)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
x=int(input())
root = buildLevelTree(levelOrder)
print(countNodesGreaterThanX(root, x))
