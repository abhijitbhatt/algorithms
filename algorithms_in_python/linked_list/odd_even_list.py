# https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional,List
import unittest
class ListNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_ptr, even_ptr, even_head_ptr = head, head.next, head.next
        while even_ptr and even_ptr.next:
            even_ptr.next, odd_ptr.next = even_ptr.next.next, odd_ptr.next.next
            even_ptr, odd_ptr = even_ptr.next, odd_ptr.next
        odd_ptr.next = even_head_ptr

def print_list(ptr: Optional[ListNode])->List[ListNode]:
    results = []
    while ptr:
        results.append(ptr.value)
        ptr = ptr.next
    return results

class TestOddEvenList(unittest.TestCase):
    def test_list_of_odd_length(self):
        head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
        Solution().oddEvenList(head)
        assert print_list(head) == [1,3,5,2,4]
    def test_list_of_even_length(self):
        head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
        Solution().oddEvenList(head)
        assert print_list(head) == [1,3,5,2,4,6]
