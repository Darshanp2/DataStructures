"""
Date: 1/21/2023

Core: Data Structures - Binary Search Tree

Topic: Converting a Binary Search Tree to Balanced Binary Search Tree

Converting a BST to Balanced BST using inorder traversal
Complexity : O(n)

"""

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def preorder(temp):
    if temp is None:
        return temp
    print(temp.data, end=" ")
    preorder(temp.left)
    preorder(temp.right)

def storeBSTNodes(root, nodes):
    if not root:
        return

    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)

def buildTreeUtil(nodes, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2
    node = nodes[mid]

    node.left = buildTreeUtil(nodes, start, mid-1)
    node.right = buildTreeUtil(nodes, mid+1, end)
    return node

def buildTree(root):
    if root is None:
        return root

    nodes = []
    storeBSTNodes(root, nodes)
    n = len(nodes)
    return buildTreeUtil(nodes, 0, n-1)

if __name__ == "__main__":
    root = newNode(6)
    root.left = newNode(5)
    root.left.left = newNode(4)
    root.left.left.left = newNode(9)
    root.left.left.left.left = newNode(10)
    root = buildTree(root)
    preorder(root)

