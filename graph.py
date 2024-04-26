"""
Date: 1/21/2023

Core: Data Structures - Graphs

Topic: Representation of Graph through adjaceny list

Array of Linked List

"""

class vertex:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.nV = vertices
        self.graph_arr = [None] * self.nV

    def add_edge(self, src, dest):
        node = vertex(dest)
        node.next = self.graph_arr[src]
        self.graph_arr[src] = node

        node = vertex(src)
        node.next = self.graph_arr[dest]
        self.graph_arr[dest] = node

    def print_graph(self):
        for i in range(self.nV):
            print("List of vertex {}\n ".format(i),end="")
            temp = self.graph_arr[i]
            while(temp):
                print(" ->  {}".format(temp.vertex),end="")
                temp = temp.next
            print("\n")
            
if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(3,2)
    graph.print_graph()
    
    

