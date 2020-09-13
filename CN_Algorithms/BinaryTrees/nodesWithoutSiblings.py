import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    # Given a binary tree, print all nodes that don’t have a sibling. Print the
    # elements in different lines. And order of elements doesn't matter.
    #############################
    # Logic is if you are standing at a root , then if one the left child or the right child is None
    # then the node that ids not None does not have a sibling
    #############################

    if root is None:
        return
    if root.left is None and root.right is None:
        return
    if root.left is None or root.right is None:
        if root.left is not None:
            print(root.left.data)
        else:
            print(root.right.data)

    nodesWithoutSibling(root.left)
    nodesWithoutSibling(root.right)

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
root = buildLevelTree(levelOrder)
nodesWithoutSibling(root)


'''
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
9 
'''