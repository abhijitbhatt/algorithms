from typing import List
import unittest
import random

def heapify(array:List[int], idx:int, max_idx:int):
    left = 2 * idx + 1
    right = 2 * idx + 2
    largest_idx = idx
    if left < max_idx and array[left] > array[idx]:
        largest_idx = left
    if right < max_idx and array[right] > array[largest_idx]:
        largest_idx = right
    if idx != largest_idx:
        array[idx], array[largest_idx] = array[largest_idx], array[idx]
        heapify(array, largest_idx, max_idx)

def make_heap(array:List[int]):
    n = len(array)
    for i in list(reversed(range(n // 2))):
        heapify(array,i,len(array))

def heap_sort(array:List[int]):
    make_heap(array)
    for i in range(len(array) - 1,0,-1):
        array[i], array[0] = array[0], array[i]
        heapify(array,0,i)


class TestHeapSort(unittest.TestCase):
    def test_even_length_reverse_sorted_array(self):
        array = list(reversed(range(1,15)))
        heap_sort(array)
        assert array == list(range(1,15))

    def test_even_length_sorted_array(self):
        array = list(range(1,15))
        heap_sort(array)
        assert array == list(range(1,15))
    def test_odd_length_reverse_sorted_array(self):
        array = list(reversed([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
        heap_sort(array)
        assert array == list(range(1,16))
    def test_odd_length_sorted_array(self):
        array = list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        heap_sort(array)
        assert array == list(range(1,16))

    def test_unsorted_array(self):
        array = []
        for i in range(random.randint(20, 100)):
            x = random.randint(0,1000)
            if i not in array:
                array.append(x)
        expected = sorted(array)
        heap_sort(array)
        assert array == expected