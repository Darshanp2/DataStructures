"""

Max Depth or Height of a Binary Tree
Time Complexity: O(N)

"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def maxDepth(Node):
    if Node is None:
        return 0
    else:
        lDepth = maxDepth(Node.left)
        rDepth = maxDepth(Node.right)

        if(lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
Depth = maxDepth(root)
print("Max Depth or Height of the tree", Depth)