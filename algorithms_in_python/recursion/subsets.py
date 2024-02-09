# https://www.geeksforgeeks.org/printing-all-subsets-of-123-n-without-using-array-or-loop/
from typing import List

def subsets(nums:List[int])->List[List[int]]:
    if len(nums) == 0:
        return [[]]
    else:
        s = subsets(nums[1:])
        return [x for x in s] + [x + [nums[0]] for x in s]

print(subsets([1,2,3]))
