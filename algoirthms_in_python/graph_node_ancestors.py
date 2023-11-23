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
