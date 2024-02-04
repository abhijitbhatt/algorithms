# https://www.geeksforgeeks.org/remove-every-k-th-node-linked-list/
import unittest
from typing import List

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next=next

def remove_kth_node(head:Node,k:int):
    if not head:
        return head
    else:
        node_count = 0
        prev = None
        start = head
        while start:
            node_count += 1
            remainder = node_count % k
            if remainder == 0: # Node to be removed
                if prev:
                    prev.next = start.next
                start = start.next
                if not prev:
                    head.next = None
                    head = start
            else:
               prev = start
               start = start.next
        return head

def convert_to_list(head:Node)->List[int]:
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

class TestRemoveKthNode(unittest.TestCase):
    def test_remove_every_2nd_node(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9)))))))))
        head = remove_kth_node(head,2)
        assert convert_to_list(head) == [1,3,5,7,9]
    def test_remove_every_3rd_node(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9)))))))))
        head = remove_kth_node(head,3)
        assert convert_to_list(head) == [1,2,4,5,7,8]
    def test_remove_every_4th_node(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9)))))))))
        head = remove_kth_node(head,4)
        assert convert_to_list(head) == [1,2,3,5,6,7,9]
    def test_remove_every_1st_node(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9)))))))))
        head = remove_kth_node(head,1)
        assert convert_to_list(head) == []