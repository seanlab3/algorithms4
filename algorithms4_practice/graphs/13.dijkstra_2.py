# def printDist(dist, V):
# 	print("\nVertex Distance")
# 	for i in range(V):
# 		if dist[i] != float('inf') :
# 			print(i,"\t",int(dist[i]),end = "\t")
# 		else:
# 			print(i,"\t","INF",end="\t")
# 		print()
#
# def minDist(mdist, vset, V):
# 	minVal = float('inf')
# 	minInd = -1
# 	for i in range(V):
# 		if (not vset[i]) and mdist[i] < minVal :
# 			minInd = i
# 			minVal = mdist[i]
# 	return minInd
#
# def Dijkstra(graph, V, src):
# 	mdist=[float('inf') for i in range(V)]
# 	vset = [False for i in range(V)]
# 	mdist[src] = 0.0
#
# 	for i in range(V-1):
# 		u = minDist(mdist, vset, V)
# 		vset[u] = True
#
# 		for v in range(V):
# 			if (not vset[v]) and graph[u][v]!=float('inf') and mdist[u] + graph[u][v] < mdist[v]:
# 				mdist[v] = mdist[u] + graph[u][v]
#
#
#
# 	printDist(mdist, V)
#


# if __name__ == "__main__":
"""

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

g.dijkstra(0);
9
28

0 1 4
0 7 8
1 0 4
1 2 8
1 7 11
2 1 8
2 3 7
2 5 4
2 8 2
3 2 7
3 4 9
3 5 14
4 3 9
4 5 10
5 2 4
5 3 14
5 4 10
5 6 2
6 5 2
6 7 1
6 8 6
7 0 8
7 1 11
7 6 1
7 8 7
8 2 2
8 6 6
8 7 7

0

Enter shortest path source:0

Vertex Distance
0 	 0
1 	 4
2 	 12
3 	 19
4 	 21
5 	 11
6 	 9
7 	 8
8 	 14

"""

from algorithms4.graphs import dijkstra_2


V = int(input("Enter number of vertices: ").strip())
E = int(input("Enter number of edges: ").strip())

graph = [[float('inf') for i in range(V)] for j in range(V)]

for i in range(V):
	graph[i][i] = 0.0

for i in range(E):
	print("\nEdge ",i+1)
	src = int(input("Enter source:").strip())
	dst = int(input("Enter destination:").strip())
	weight = float(input("Enter weight:").strip())
	graph[src][dst] = weight

gsrc = int(input("\nEnter shortest path source:").strip())
dijkstra_2.Dijkstra(graph, V, gsrc)
