# Root vertex of a graph: https://www.techiedelight.com/root-vertex-graph/
from enum import Enum
from collections import defaultdict
import unittest

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2

class DiGraph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)
    def add_edge(self,u,v):
        self.adj_list[u].append(v)

class RootVertex:
    def __init__(self,graph):
        self.graph = graph
        self.color = [Color.WHITE] * len(self.graph.nodes)

    def find_root(self):
        root_nodes = []
        def dfs(u):
            self.color[u] = Color.GREY
            for neighbor in self.graph.adj_list[u]:
                if self.color[neighbor] == Color.WHITE:
                    dfs(neighbor)
            self.color[u] = Color.BLACK
        for n in self.graph.nodes:
            if self.color[n] == Color.WHITE:
                dfs(n)
            if sum([1 for c in self.color if c == Color.WHITE]) > 0:
                continue
            else:
                root_nodes.append(n)

        for r in root_nodes:
            self.color = [Color.WHITE] * len(self.graph.nodes)
            dfs(r)
            if sum([1 for c in self.color if c == Color.WHITE]) > 0:
                continue
            else:
                return r
        return None

class TestRootVertex(unittest.TestCase):
    def test_graph_without_root(self):
        graph = DiGraph([3,2,1,0,4,5])
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(4,3)
        graph.add_edge(4,5)
        self.assertEqual(RootVertex(graph).find_root(),None)

    def test_graph_with_one_root(self):
        graph = DiGraph([3,2,1,0,5,4])
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(4,3)
        graph.add_edge(4,5)
        graph.add_edge(5,0)
        graph.add_edge(3,0)
        self.assertTrue(RootVertex(graph).find_root() == 4)

    def test_graph_with_multiple_roots(self):
        graph = DiGraph([3,2,1,0,5,6,4])
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(3,0)
        graph.add_edge(4,3)
        graph.add_edge(4,5)
        graph.add_edge(5,0)
        graph.add_edge(6,4)
        self.assertTrue(RootVertex(graph).find_root() == 6)

TestRootVertex()

