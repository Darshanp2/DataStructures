"""
Binary Tree - Array Implementation 

Left child - 2*parent + 1
Right child - 2*parent + 2

Time Complexity: 0(logn)
"""

tree = [None]*10

def root(key):
    if tree[0] != None:
        print("Root already exist")
    else:
        tree[0] = key
    
def left(key, parent):
    if tree[parent] == None:
        print("Parent doesn't exist for", (2*parent) + 1, "node")
    else:
        tree[2*parent+1] = key

def right(key, parent):
    if tree[parent] == None:
        print("Parent doesn't exist for", (2*parent) + 2, "node")
    else:
        tree[2*parent+2] = key

def printTree():
    for i in range(len(tree)):
        if tree[i] != None:
            print(tree[i],end="")
        else:
            print('-',end="")

root('A')
left('B',0)
right('C',0)
left('D', 1)

left('F',2)
right('G',2)
printTree()

