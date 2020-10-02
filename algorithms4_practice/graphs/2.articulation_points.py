# # Finding Articulation Points in Undirected Graph
# def computeAP(l):
#     n = len(l)
#     outEdgeCount = 0
#     low = [0] * n
#     visited = [False] * n
#     isArt = [False] * n
#
#     def dfs(root, at, parent, outEdgeCount):
#         if parent == root:
#             outEdgeCount += 1
#         visited[at] = True
#         low[at] = at
#
#         for to in l[at]:
#             if to == parent:
#                 pass
#             elif not visited[to]:
#                 outEdgeCount = dfs(root, to, at, outEdgeCount)
#                 low[at] = min(low[at], low[to])
#
#                 # AP found via bridge
#                 if at < low[to]:
#                     isArt[at] = True
#                 # AP found via cycle
#                 if at == low[to]:
#                     isArt[at] = True
#             else:
#                 low[at] = min(low[at], to)
#         return outEdgeCount
#
#     for i in range(n):
#         if not visited[i]:
#             outEdgeCount = 0
#             outEdgeCount = dfs(i, i, -1, outEdgeCount)
#             isArt[i] = (outEdgeCount > 1)
#
#     for x in range(len(isArt)):
#         if isArt[x] == True:
#             print(x)
#
# # Adjacency list of graph
from algorithms4.graphs import articulation_points


l = {0:[1,2], 1:[0,2], 2:[0,1,3,5], 3:[2,4], 4:[3], 5:[2,6,8], 6:[5,7], 7:[6,8], 8:[5,7]}
from collections import defaultdict
d=defaultdict(list)
for i in range(20):
    n,m=map(int,input().split())
    d[n].append(m)
"""
0 1
0 2
1 0
1 2
2 0
2 1
2 3
2 5
3 2
3 4
4 3
5 2
5 6
5 8
6 5
6 7
7 6 
7 8
8 5
8 7

"""
articulation_points.computeAP(l)

articulation_points.computeAP(d)
