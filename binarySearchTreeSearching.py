"""
Date: 1/20/2023

Core: Data Structures - Binary Search Tree

Topic: Searching in a Binary Search Tree

Complexity: O(n)
"""

class newNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.data,end=" ")
    inorder(temp.right)

def insert(root, key):
    if root is None:
        root = newNode(key)
    else:
        if root.data == key:
            return root
        else:
            if root.data > key:
                root.left = insert(root.left, key)
            else:
                root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None:
        return None
    else:
        if root.data is key:
            return root.data
        else:
            if root.data > key:
                return search(root.left, key)
            else:
                return search(root.right, key)
    
if __name__ == "__main__":
    root = newNode(1)
    insert(root,2)
    insert(root,3)
    inorder(root)