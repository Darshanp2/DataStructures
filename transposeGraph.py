"""
Date: 1/21/2023

Core: Data Structures - Graph

Topic: Transpose of a Graph

"""
def addEdge(adj, src, dest):
	adj[src].append(dest)

def displayGraph(adj, v):
	for i in range(v):
		print(i, "--> ", end = "")
		for j in range(len(adj[i])):
			print(adj[i][j], end = " ")
		print()

def transposeGraph(adj, transpose, v):	
	for i in range(v):
		for j in range(len(adj[i])):
			addEdge(transpose, adj[i][j], i)

if __name__ == '__main__':

	v = 5
	adj = [[] for i in range(v)]
	addEdge(adj, 0, 1)
	addEdge(adj, 0, 4)
	addEdge(adj, 0, 3)
	addEdge(adj, 2, 0)
	addEdge(adj, 3, 2)
	addEdge(adj, 4, 1)
	addEdge(adj, 4, 3)

	transpose = [[]for i in range(v)]
	transposeGraph(adj, transpose, v)

	displayGraph(transpose, v)

