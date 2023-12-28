# Peak element in array
# https://www.techiedelight.com/find-peak-element-array/
from typing import List

def peak_element(array:List[int])->int:
    def peak_element_recursive(start:int, end:int)->int:
        if start > end:
            return array[end]
        mid = (start + end) // 2
        if mid - 1 >= 0 and mid + 1 <= len(array) - 1:
            if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
                return mid
            elif array[mid] < array[mid - 1]:
                return peak_element_recursive(start, mid - 1)
            else:
                return peak_element_recursive(mid + 1, end)
        else:
            return mid
    return peak_element_recursive(0, len(array) - 1)

print(peak_element([8, 9, 10, 2, 5, 6]))