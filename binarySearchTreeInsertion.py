"""
Date: 1/19/2023

Core: Data Structures - Binary Search Tree

Topic: Insertion in a Binary Search Tree using Recursion 

Complexity : O(n)

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.data,end="")
    inorder(temp.right)

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    
    return root


if __name__ == "__main__":
    root = Node(1)
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 3)
    
    inorder(root)
