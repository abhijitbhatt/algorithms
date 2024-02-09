import random
from typing import List

def partition(nums:List[int],start:int,end:int):
    pivot_index = j = start
    for i in range(start + 1, end + 1):
        if nums[i] > nums[pivot_index]:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
    return j

def find_kth_largest(nums,k):
    start = 0
    end = len(nums) - 1
    pivot_index = partition(nums,0,len(nums) - 1)
    while pivot_index != k:
        if k > pivot_index:
            start = pivot_index + 1
        else:
            end = pivot_index - 1

        pivot_index = partition(nums,start, end)
    print(nums[k])

nums = [90, 72, 19, 55, 11, 86, 63, 37, 26, 85]
print(sorted(nums, key=lambda x: -x))
find_kth_largest(nums,5)
