from typing import List
from collections import defaultdict

def dup_freq(array:List[int]):
    freq = defaultdict(int)
    def dup_freq_recursive(start:int, end:int):
        if start > end:
            return
        mid = (start + end) // 2
        freq[array[mid]] += 1
        if array[start] == array[mid]:
            freq[array[start]] += (mid - start )
        else:
            dup_freq_recursive(start, mid - 1)
        if array[mid] == array[end]:
            freq[array[start]] += (end - mid)
        else:
            dup_freq_recursive(mid + 1, end)
    dup_freq_recursive(0,len(array) - 1)
    return freq

print(dup_freq([2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]))

#print(dup_freq([0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5]))
