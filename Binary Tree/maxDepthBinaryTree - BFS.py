"""
maxDepth or Height of Binary Tree - Bread First Search Traversal (BFS)

Time Complexity: O(N)

"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(Node):
    if Node is None:
        return 0

    inorder(Node.left)
    print(Node.key, end="")
    inorder(Node.right)

def maxDepth(root):

    q = []
    q.append(root)
    height = 0 

    while q:
        nodecount = len(q)
        while nodecount > 0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            nodecount -= 1
        height += 1
    return height

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)
height = maxDepth(root)
print("\n")
print("Height of the tree", height)