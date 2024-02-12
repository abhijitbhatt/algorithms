
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def is_palindrome(head:Node)->bool:
    ptr = head
    def is_palindrome_recursive(head:Node)->bool:
        nonlocal ptr
        if not head:
            return True
        else:
            tmp = head.value
            if not is_palindrome_recursive(head.next):
                return False
            if tmp != ptr.value:
                return False
            else:
                ptr = ptr.next
                return True
    return is_palindrome_recursive(head)
head = Node(1,Node(2,Node(2,Node(1))))
print(is_palindrome(head))
