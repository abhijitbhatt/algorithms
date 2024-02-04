
import unittest
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


def find_middle_elemenet(head:Node):
    if not head:
        return None
    elif not head.next:
        return head.value
    elif not head.next.next:
        return head.next.value
    prev_ptr = None
    ptr = head
    while ptr.next is not None and ptr.next.next is not None:
        prev_ptr = head if not prev_ptr else prev_ptr.next
        ptr = ptr.next.next
    return prev_ptr.next.value

class TestMiddleElementOfLinkedList(unittest.TestCase):
    def test_empty_linked_list(self):
        head = None
        assert find_middle_elemenet(head) is None
    def test_linked_list_with_1_node(self):
        head = Node(1)
        assert find_middle_elemenet(head) == 1
    def test_linked_list_with_2_nodes(self):
        head = Node(1,Node(2))
        assert find_middle_elemenet(head) == 2
    def test_linked_list_with_5_nodes(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5)))))
        assert find_middle_elemenet(head) == 3
    def test_linked_list_with_6_nodes(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
        assert find_middle_elemenet(head) == 3
    def test_linked_list_with_7_nodes(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
        assert find_middle_elemenet(head) == 4