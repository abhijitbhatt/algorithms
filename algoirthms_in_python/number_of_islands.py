from enum import Enum
from collections import defaultdict
class Color(Enum):
    WHITE=0
    GREY=2
    BLACK=2

class Graph:
    def __init__(self,adj_matrix):
        self.row = len(adj_matrix)
        self.column = len(adj_matrix[0])
        self.nodes = {}
        node_num = 0
        self.adj_list = defaultdict(list)
        for i in range(0,len(adj_matrix)):
            for j in range(0,len(adj_matrix[i])):
                if adj_matrix[i][j] == 0: continue
                for k in [-1,0,1]:
                    if i + k < 0 or i + k > len(adj_matrix) - 1: continue
                    for l in [-1,0,1]:
                        if k == 0 and l == 0: continue
                        if j + l < 0 or j + l > len(adj_matrix[i]) - 1: continue
                        if adj_matrix[i + k][j + l] == 0: continue
                        if i * self.column + j not in self.nodes:
                            self.nodes[i * self.column + j] = node_num
                            node_num += 1
                        u = self.nodes[i * self.column + j]
                        if (i + k) * self.column + j + l not in self.nodes:
                            self.nodes[(i + k) * self.column + j + l] = node_num
                            node_num += 1
                        v = self.nodes[(i + k) * self.column + j + l]
                        self.adj_list[u].append(v)
class IslandCount:
    def __init__(self,graph):
        self.graph = graph
        self.color = [Color.WHITE] * len(graph.nodes.values())
        self.parents = [None] * len(graph.nodes.values())

    def dfs(self):
        cc = 0
        def dfs_recursive(x):
            self.color[x] = Color.GREY
            for neighbor in self.graph.adj_list[x]:
                if self.color[neighbor] == Color.WHITE:
                    self.parents[neighbor] = x
                    dfs_recursive(neighbor)
            self.color[x] = Color.BLACK

        for u in self.graph.nodes.values():
            if self.color[u] == Color.WHITE:
                cc += 1
                dfs_recursive(u)
        return cc

graph = Graph(
    [[1,1,0,0,1,0,1],
     [0,1,0,1,1,0,1],
     [0,0,0,0,0,0,0],
     [0,1,1,0,0,0,0],
     [1,0,1,0,0,1,0],
     [1,0,0,0,1,1,0]]
)

print(graph.nodes)
print(graph.adj_list)
print(IslandCount(graph).dfs())