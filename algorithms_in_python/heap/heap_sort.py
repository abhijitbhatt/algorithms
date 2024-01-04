from typing import List

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
    for i in range(len(array) // 2, -1 , -1):
        heapify(array,i,len(array))

def heap_sort(array:List[int]):
    make_heap(array)
    for i in range(len(array) - 1,0,-1):
        array[i], array[0] = array[0], array[i]
        heapify(array,0,i)

#array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15][::-1]
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(array)
heap_sort(array)
print(array)
