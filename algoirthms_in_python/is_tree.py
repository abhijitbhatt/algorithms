# Detect cycle in undirected graph
# https://www.techiedelight.com/determine-undirected-graph-tree-acyclic-connected-graph/
from enum import Enum
from collections import defaultdict
import unittest

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

class IsTree:
    def __init__(self,graph):
        self.graph = graph
        self.color = [Color.WHITE] * len(self.graph.nodes)
        self.parent = [None] * len(self.graph.nodes)
    def check_cycle(self):
        def check_cycle_recursive(u):
            self.color[u] = Color.GREY
            for neighbor in self.graph.adj_list[u]:
                if self.color[neighbor] == Color.WHITE:
                    self.parent[neighbor] = u
                    if check_cycle_recursive(neighbor):
                        return True
                elif self.color[neighbor] == Color.GREY and self.parent[u] != neighbor:
                    return True
            self.color[u] = Color.BLACK
            return False
        cc = 1
        for n in self.graph.nodes:
            if self.color[n] == Color.WHITE:
                if cc > 1:
                    # The graph has more than one connected component
                    return True
                if check_cycle_recursive(n):
                    return True
                else:
                    cc += 1

        return False

class TestIsTree(unittest.TestCase):
    def test_graph_wo_cycle(self):
        graph = Graph(range(6))
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(3,4)
        graph.add_edge(4,5)
        self.assertTrue(not IsTree(graph).check_cycle())

    def test_graph_with_cycle(self):
        graph = Graph(range(6))
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(3,4)
        graph.add_edge(4,5)
        graph.add_edge(5,0)
        self.assertTrue(IsTree(graph).check_cycle())

    def test_graph_with_more_one_cc(self):
        graph = Graph(range(6))
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(3,4)
        graph.add_edge(4,5)
        self.assertTrue(IsTree(graph).check_cycle())

if __name__ == '__main__':
    unittest.main()