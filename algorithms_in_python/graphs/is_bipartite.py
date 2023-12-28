from enum import Enum
from collections import defaultdict
import unittest
class Color(Enum):
    WHITE=0
    GREY=1
    BLACK=2
    RED=3
    BLUE=4
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = defaultdict(list)
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

class Bipartite:
    def __init__(self,graph):
        self.graph = graph
        self.visited = [Color.WHITE] * len(self.graph.nodes)
        self.parent = [None] * len(self.graph.nodes)
        self.color = [None] * len(self.graph.nodes)
    def check(self):
        def check_recursive(u):
            self.visited[u] = Color.GREY
            for neighbor in self.graph.adj_list[u]:
                if self.visited[neighbor] == Color.WHITE:
                    self.parent[neighbor] = u
                    self.color[neighbor] = Color.RED if self.color[u] == Color.BLUE else Color.BLUE
                    if not check_recursive(neighbor):
                        return False
                else:
                    if self.color[u] == self.color[neighbor]:
                        return False
            self.visited[u] = Color.BLACK
            return True
        for n in self.graph.nodes:
            if self.visited[n] == Color.WHITE:
                self.color[n] = Color.RED
                if not check_recursive(n):
                    return False
        return True

class TestBipartite(unittest.TestCase):
    def test_cycle_with_odd_nodes(self):
        graph = Graph(range(5))
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(3,4)
        graph.add_edge(4,0)
        self.assertFalse(Bipartite(graph).check())

    def test_star_graph(self):
        graph = Graph(range(6))
        graph.add_edge(0,1)
        graph.add_edge(0,2)
        graph.add_edge(0,3)
        graph.add_edge(0,4)
        graph.add_edge(0,5)
        self.assertTrue(Bipartite(graph).check())

if __name__ == '__main__':
    unittest.main()
