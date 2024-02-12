
from typing import List
def subarrays(nums:List[int])->List[List[int]]:
    results = []
    def subarray_recursive(nums:List[int],start:int=0,end:int=1)->None:
        if start == len(nums):
            return
        if end == len(nums) + 1:
            return
        results.append(nums[start:end])
        if end == len(nums):
            subarray_recursive(nums,start + 1,start + 2)
        else:
            subarray_recursive(nums,start,end + 1)
    subarray_recursive(nums)
    return results

def subarray_nonrecursive(nums:List[int])->List[List[int]]:
    results = []
    for i in range(0,len(nums)):
        for j in range(i + 1,len(nums) + 1):
            results.append(nums[i:j])
    print(results)

nums = [1,2,3,4,5]
#print(subarray_nonrecursive(nums))
print(subarrays(nums))
