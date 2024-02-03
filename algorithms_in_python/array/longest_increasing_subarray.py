import unittest
def longest_common_subarray(nums):
    max_len_so_far = len_so_far = 1
    right_bound = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i - 1]:
            len_so_far += 1
        else:
            if len_so_far > max_len_so_far:
                max_len_so_far = len_so_far
                right_bound = i
            len_so_far = 1
    if len_so_far > max_len_so_far:
        max_len_so_far = len_so_far
        right_bound = len(nums)
    return max_len_so_far, nums[right_bound - max_len_so_far:right_bound]

class TestLongestCommonSubarray(unittest.TestCase):
    def test_longest_common_subarray_ends_before_last_element(self):
        assert longest_common_subarray([5, 6, 3, 5, 7, 8, 9, 1, 2]) == (5, [3,5,7,8,9])
    def test_longest_common_subarray_ends_at_last_element(self):
        assert longest_common_subarray([5, 6, 3, 5, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]) == (7, [1, 2, 3, 4, 5, 6, 7])

