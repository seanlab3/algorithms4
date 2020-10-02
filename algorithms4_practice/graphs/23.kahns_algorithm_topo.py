# Kahn's Algorithm is used to find Topological ordering of Directed Acyclic Graph using BFS
# def topologicalSort(l):
#     indegree = [0] * len(l)
#     queue = []
#     topo = []
#     cnt = 0
#
#     for key, values in l.items():
#         for i in values:
#             indegree[i] += 1
#
#     for i in range(len(indegree)):
#         if indegree[i] == 0:
#             queue.append(i)
#
#     while(queue):
#         vertex = queue.pop(0)
#         cnt += 1
#         topo.append(vertex)
#         for x in l[vertex]:
#             indegree[x] -= 1
#             if indegree[x] == 0:
#                 queue.append(x)
#
#     if cnt != len(l):
#         print("Cycle exists")
#     else:
#         print(topo)
#
# # Adjacency List of Graph
# l = {0:[1,2], 1:[3], 2:[3], 3:[4,5], 4:[], 5:[]}
# topologicalSort(l)
from algorithms4.graphs import kahns_algorithm_topo
from collections import defaultdict

l = {0:[1,2], 1:[3], 2:[3], 3:[4,5], 4:[], 5:[]}
kahns_algorithm_topo.topologicalSort(l)
"""
0 1
0 2
1 3
2 3
3 4
3 5
4 0 
5 0

"""
d=defaultdict(list)
for i in range(8):
    n,m=map(int,input().split())
    if m==0:
        d[n]
    else:
        d[n].append(m)
print(d)
kahns_algorithm_topo.topologicalSort(d)

