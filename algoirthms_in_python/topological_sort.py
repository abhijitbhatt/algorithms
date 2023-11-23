# Topological sort using recursive DFS
# Also detects presence of cycle and throws exception
from enum import Enum
from collections import defaultdict
from typing import List
import unittest
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

class TopologicalSort:
    def __init__(self,graph):
        self.graph = graph
        self.color = [Color.WHITE] * len(self.graph.nodes)
    def sort(self)->List[int]:
        # Additional data structure for topological sort
        # Node is pushed into stack only when all its neighbors are visited
        # In other words when the node is colored black
        stack = []
        def sort_recursive(u):
            self.color[u] = Color.GREY
            for neighbor in self.graph.adj_list[u]:
                if self.color[neighbor] == Color.WHITE:
                    sort_recursive(neighbor)
                elif self.color[neighbor] == Color.GREY:
                    raise Exception(f"Graph contains a cycle")
            stack.append(u)
            self.color[u] = Color.BLACK
        for n in self.graph.nodes:
            if self.color[n] == Color.WHITE:
                sort_recursive(n)
        return stack[::-1]

class TestTopologicalSort(unittest.TestCase):
    def test_cycle(self):
        graph = DiGraph(range(6))
        graph.add_edge(5,0)
        graph.add_edge(5,2)
        graph.add_edge(4,0)
        graph.add_edge(4,1)
        graph.add_edge(2,3)
        graph.add_edge(1,3)
        graph.add_edge(3,5)
        s = TopologicalSort(graph)
        with self.assertRaises(Exception):
            s.sort()

    def test_dag(self):
        graph = DiGraph(range(6))
        graph.add_edge(5,0)
        graph.add_edge(5,2)
        graph.add_edge(4,0)
        graph.add_edge(4,1)
        graph.add_edge(2,3)
        graph.add_edge(1,3)
        s = TopologicalSort(graph)
        result = s.sort()
        self.assertTrue(result[0] in [5,4])
        self.assertTrue(result[5] == 3 or result[4] == 3)
if __name__ == '__main__':
    unittest.main()
