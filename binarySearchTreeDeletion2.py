"""
Date: 1/21/2023

Core: Data Structures - Binary Search Tree

Topic: Deletion in a Binary Search Tree

Complexity: O(h) where h is the height of the tree

(Instead of calling deleteNode method everytime we can keep track of the parent node of the successor)
"""

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(temp):
    if temp is None:
        return temp
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

def insert(root, key):
    if root is key:
        return root
    if root is None:
        root = newNode(key)
    else:
        if key < root.data:
            root.left = insert(root.left, key)
        elif key > root.data:
            root.right = insert(root.right, key)
    
    return root

def deleteNode(root, key):
    if root is None:
        return root
    
    if key < root.data:
        root.left = deleteNode(root.left, key)
        return root
    elif key > root.data:
        root.right = deleteNode(root.right, key)
        return root
    
    #when the root is a leaf node
    if root.left is None and root.right is None:
        return root
    
    #When the root has one child
    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    succParent = root
    succ = root.right

    while(succ.left != None):
        succParent = succ
        succ = succ.left

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    root.data = succ.data

    return root

if __name__ == "__main__":
    root = newNode(2)
    insert(root, 3)
    insert(root, 4)
    insert(root, 5)
    inorder(root)
    deleteNode(root, 4)
    print()
    inorder(root)
    