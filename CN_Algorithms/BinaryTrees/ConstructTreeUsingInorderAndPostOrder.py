from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(postOrder, inOrder, n):
    if len(postOrder) == 0:
        return None
    root_data = postOrder[-1]
    root_node = BinaryTreeNode(root_data)

    rootIndex_in = inOrder.index(root_data)

    leftSubtree_in = inOrder[:rootIndex_in]
    rightSubtree_in = inOrder[rootIndex_in+1:]

    leftSubTreeLen_in = len(leftSubtree_in)
    leftSubtree_post = postOrder[:leftSubTreeLen_in]
    rightSubtree_post = postOrder[leftSubTreeLen_in:len(postOrder)-1]

    root_node.left = buildTree(leftSubtree_post, leftSubtree_in, n-1)
    root_node.right = buildTree(rightSubtree_post, rightSubtree_in, n-1)

    return root_node



'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)

'''
7
4 5 2 6 7 3 1 
4 2 5 1 6 3 7 

1 
2 3 
4 5 6 7 
'''