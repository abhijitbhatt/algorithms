from typing import List
import random
import unittest

def heapify(array:List[int], index:int, max_index:int)->None:
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    largest_index = index
    if left_child < max_index and array[left_child] > array[index]:
        largest_index = left_child
    if right_child < max_index and array[largest_index] < array[right_child]:
        largest_index = right_child
    if index != largest_index:
        array[index], array[largest_index] = array[largest_index], array[index]

def make_heap(array:List[int],n:int)->None:
    for i in reversed(range(0, n // 2)):
        heapify(array, i, n)

def kth_largest(array:List[int],k:int)->int:
    make_heap(array,k)
    for i in range(k + 1, len(array)):
        if array[i] < array[0]:
            array[0] = array[i]
            make_heap(array,k)
    return array[0]

class TestKthLargest(unittest.TestCase):
    def test_10th_largest_element(self):
        array = list(range(1,101))
        random.shuffle(array)
        assert kth_largest(array,10) == 10

    def test_100th_largest_element(self):
        array = list(range(1,101))
        random.shuffle(array)
        assert kth_largest(array,100) == 100