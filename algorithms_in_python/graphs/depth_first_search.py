# Working with algorithms in Python - Video series by George T. Heineman
from collections import defaultdict
from enum import Enum

class Color(Enum):
    WHITE = 1
    GREY = 2
    BLACK = 3

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def add_edges(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

class GraphTraversal:
    def __init__(self,g):
        self.graph = g
        self.parents = [None] * len(g.nodes)
        self.colors = [Color.WHITE] * len(g.nodes)

    def dfs(self,u):
        self.colors[u] = Color.GREY
        for neighbor in self.graph.adj_list[u]:
            if self.colors[neighbor] == Color.WHITE:
                self.parents[neighbor] = u
                self.dfs(neighbor)
        self.colors[u] = Color.BLACK

    def get_path(self,u,v):
        self.dfs(u)
        path = [v]
        while self.parents[v]:
            path.insert(0,self.parents[v])
            if u != v:
                v = self.parents[v]
        return ','.join(map(str,path))

    def is_cycle(self):
        def is_cycle_recursive(u):
            self.colors[u] = Color.GREY
            for neighbor in self.graph.adj_list[u]:
                if self.colors[neighbor] == Color.WHITE:
                    self.parents[neighbor] = u
                    if is_cycle_recursive(neighbor):
                        return True
                elif self.colors[neighbor] == Color.GREY:
                    if neighbor != self.parents[u]:
                        return True
            else:
                self.colors[u] = Color.BLACK
                return False

        for u in self.graph.nodes:
            if self.colors[u] == Color.WHITE:
                result = is_cycle_recursive(u)
                if result:
                    return True
        return False

    def count_connected_components(self):
        cc = 0
        for u in self.graph.nodes:
            if self.colors[u] == Color.WHITE:
                self.dfs(u)
                cc += 1
        return cc

g = Graph(range(8))
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(2,3)
g.add_edges(2,4)
g.add_edges(4,5)
g.add_edges(5,6)
g.add_edges(6,7)
g.add_edges(3,5)
g.add_edges(3,6)

# Initialize traversal
traversal = GraphTraversal(g)
print(traversal.get_path(0,6))
#print(traversal.dfs(0))
#print(traversal.parents)