# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
from typing import List,Tuple

# recursive method to generate all subarrays
# Used in brute force method
def all_subarrays(nums:List[int])->List[List[int]]:
    results = []
    def all_subarrays_recursive(nums:List[int],i:int=0,j:int=1)->None:
        if i == len(nums):
            return
        if j == len(nums) + 1:
            return
        results.append(nums[i:j])
        if j == len(nums):
            all_subarrays_recursive(nums,i + 1, i + 2)
        else:
            all_subarrays_recursive(nums,i,j + 1)
    all_subarrays_recursive(nums,0,1)
    return results

# Largest subarray by brute force method
def largest_subarray_brute_force(nums:List[int])->Tuple:
    max_sum = float('-inf')
    max_index = -1
    sub_arrays = all_subarrays(nums)
    for i,e in enumerate(sub_arrays):
        if max_sum < sum(e):
            max_sum = sum(e)
            max_index = i
    return max_sum,sub_arrays[max_index]

def longest_subarray(nums:List[int])->Tuple:
    sum_so_far = nums[0]
    max_sum_so_far = float('-inf')
    for i in range(1,len(nums)):
        if nums[i] + sum_so_far > nums[i]:
            sum_so_far = nums[i] + sum_so_far
        else:
            sum_so_far = nums[i]
        max_sum_so_far = max(max_sum_so_far, sum_so_far)
    print(max_sum_so_far)

nums = [-2,-3,4,-1,-2,1,5,-3]
#print(longest_subarray_brute_force(nums))
print(longest_subarray(nums))