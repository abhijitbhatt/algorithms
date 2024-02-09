# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
import unittest
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_total = float('-inf')
        for i in range(0,len(nums) - k + 1):
            if i == 0:
                current_total = sum(nums[i:i+k])
            else:
                # Use last sum to derive the next sum
                # drop left most element and add right most one
                current_total = current_total - nums[i - 1] + nums[i + k - 1]
            max_total = max(max_total,current_total)
        # Compute average at the end
        return max_total * 1.0 / k

class TestFindMaxAverage(unittest.TestCase):
    def test_single_element_array(self):
        assert Solution().findMaxAverage([5],1) == 5.0
    def test_multiple_element_array(self):
        assert Solution().findMaxAverage([1,12,-5,-6,50,3],4) == 12.75




#Input: nums = [1,12,-5,-6,50,3], k = 4
#Output: 12.75000
#Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75