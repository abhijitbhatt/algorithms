import random
def quicksort_with_extra_storage(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less_than_pivot = [x for x in nums[1:] if x < pivot]
        greater_than_pivot = [x for x in nums[1:] if x >= pivot]
        return quicksort_with_extra_storage(less_than_pivot) + [nums[0]] + quicksort_with_extra_storage(greater_than_pivot)

def partition(nums,start,end):
    pivot = nums[start]
    j = start
    for i in range(start + 1, end + 1):
        if nums[i] < pivot:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[j], nums[start] = nums[start], nums[j]
    return j

def quicksort(nums,start,end):
    if start > end:
        return
    else:
        pivot_index = partition(nums,start,end)
        quicksort(nums,start,pivot_index - 1)
        quicksort(nums,pivot_index + 1,end)


nums = [55, 19, 70, 96, 75, 43, 4, 45, 61, 24]
quicksort(nums,0,len(nums) - 1)
print(nums)
#print(quicksort_with_extra_storage(nums))