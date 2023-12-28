from typing import List
import unittest

def one_count(array:List[int])->int:
    global low_index, high_index
    low_index = float('inf')
    high_index = float('-inf')
    def one_count_recursive(start:int, end:int)->int:
        global low_index, high_index
        if start > end:
            return
        else:
            mid = (start + end) // 2
            if array[mid] == 1:
                if mid < low_index:
                    low_index = mid
                if mid > high_index:
                    high_index = mid
                one_count_recursive(start, mid - 1)
                one_count_recursive(mid + 1, end)
            elif array[mid] == 0:
                one_count_recursive(mid + 1, end)
    one_count_recursive(0, len(array) - 1)
    if low_index == float('inf') and high_index == float('-inf'):
        return 0
    else:
        return high_index - low_index + 1

class TestOneCount(unittest.TestCase):
    def test_all_zeroes(self):
        assert one_count([0] * 10) == 0
    def test_all_ones(self):
        assert one_count([1] * 10) == 10
    def test_1_ones(self):
        assert one_count([0] * 10 + [1]) == 1
    def test_5_ones(self):
        assert one_count([0] * 10 + [1] * 5) == 5