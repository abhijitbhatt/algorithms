# https://www.geeksforgeeks.org/recursively-reversing-a-linked-list-a-simple-implementation/

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def reverse(head:Node)->Node:
    root = None
    def reverse_recursive(head:Node)->None:
        nonlocal root
        if not head or not head.next:
            root = head
            return
        reverse_recursive(head.next)
        head.next.next = head
    reverse_recursive(head)
    head.next = None
    return root

def print_list(head:Node):
    if not head:
        return
    while head:
        print(head.value)
        head = head.next

head = Node(1,Node(2,Node(3,Node(4))))
root = reverse(head)
print_list(root)