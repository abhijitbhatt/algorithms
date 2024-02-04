# https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/

from typing import List

def push_at_stack_bottom(stack:List[int],e:int)->None:
    if len(stack) == 0:
        stack.append(e)
    else:
        temp = stack.pop()
        push_at_stack_bottom(stack,e)
        stack.append(temp)

def reverse(stack:List[int])->None:
    if len(stack) == 0:
        return
    temp = stack.pop()
    reverse(stack)
    push_at_stack_bottom(stack,temp)

nums = [1,2,3,4]
reverse(nums)
print(nums)

