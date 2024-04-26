"""
Date: 1/18/2023

Core: Data Structures

Topic: Binary Tree Implementation using Array

""" 


tree = [None] * 10

def root(key):
    if tree[0] != None:
        print("Root already exists")
    else:
        tree[0] = key

def set_left(key, parent):
    if tree[parent] == None:
        print(" Can't set child at", (parent * 2) + 1, ",no parent found")
    else:
        tree[(parent * 2) + 1] = key

def set_right(key, parent):
    if tree[parent] == None:
        print(" Can't set child at", (parent * 2) + 2, ",no parent found")
    else:
        tree[(parent * 2) + 2] = key

def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end = "")
        else:
            print("-", end = "")
    print()
        
root('A')
set_left('B', 0)
set_right("C", 1)
print_tree()
