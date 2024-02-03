# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        max_count = 0
        count = 1
        while len(elements) > 0:
            e = elements.pop()
            tmp = e - 1
            while tmp in elements:
                count += 1
                elements.remove(tmp)
                tmp -= 1
            tmp = e + 1
            while tmp in elements:
                count += 1
                elements.remove(tmp)
                tmp += 1
            max_count = max(max_count,count)
            count = 1
        return max_count

class TestLongestConsectiveSeq(unittest.TestCase):
    def test_dup_values_with_missing_number(self):
        nums = [0,3,7,2,8,4,6,0,1]
        assert Solution().longestConsecutive(nums) == 5
    def test_no_dup_values_with_missing_number(self):
        nums = [4,7,6,1,3,2,21,20,27,26,5]
        assert Solution().longestConsecutive(nums) == 7
    def test_with_negative_number(self):
        nums = [-1,0,1]
        assert Solution().longestConsecutive(nums) == 3
    def test_one_element_out_of_order(self):
        nums = [-1,1,2,0]
        assert Solution().longestConsecutive(nums) == 4