# Number of rotations in a circular sorted array
# https://www.techiedelight.com/find-number-rotations-circularly-sorted-array/
from typing import List
def find_rotation_count(array:List[int]):
    start = 0
    end = len(array) - 1

    def find_rotation_count_recursive(start:int, end:int):
        if start > end:
            return 0
        mid = (start + end) // 2
        if mid - 1 >= 0 and mid + 1 <= end:
            if array[mid] < array[mid - 1] and array[mid] < array[mid + 1]:
                return mid
            elif array[end] > array[mid]:
                return find_rotation_count_recursive(start, mid - 1)
            else:
                return find_rotation_count_recursive(mid + 1, end)
        else:
            return 0
    return find_rotation_count_recursive(start, end)

print(find_rotation_count([6,7,8,9,10,1,2,3,4,5]))