# Problem description: https://www.geeksforgeeks.org/find-ancestors-of-each-node-in-the-given-graph/?ref=ml_lbp
from enum import Enum
from collections import defaultdict

class Color(Enum):
    WHITE=0
    GREY=1
    BLACK=2

class DiGraph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v):
        self.adj_list[u].append(v)

class NodeAncestor:
    def __init__(self,graph):
        self.graph = graph
        self.parent = [[] for _ in range(len(self.graph.nodes))]
        self.color = [Color.WHITE] * len(self.graph.nodes)

    def get_anscestor(self):
        def ancestor_recursive(u):
            self.color[u] = Color.GREY
            for neighbor in self.graph.adj_list[u]:
                if self.color[neighbor] == Color.WHITE:
                    if len(self.parent[u]) > 0:
                        self.parent[neighbor].extend([u] + self.parent[u])
                    else:
                        self.parent[neighbor] = [u]
                    ancestor_recursive(neighbor)
            self.color[u] = Color.BLACK
        for n in self.graph.nodes:
            if self.color[n] == Color.WHITE:
                ancestor_recursive(n)
        for n in range(len(self.parent)):
            if len(self.parent[n]) == 0:
                print(f'{n} -> None')
            else:
                print(f'{n} -> {self.parent[n]}')

graph = DiGraph(range(5))
graph.add_edge(0,4)
graph.add_edge(4,3)
graph.add_edge(4,1)
graph.add_edge(1,2)
NodeAncestor(graph).get_anscestor()