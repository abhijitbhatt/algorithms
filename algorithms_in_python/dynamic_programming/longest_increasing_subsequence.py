# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
from typing import List

# Dynamic programming - bottom up
def longest_increasing_subsequence_bottom_up(nums:List[int])->int:
    n = len(nums)
    dp = [1] * n
    max_len = 1
    for i in range(1,n):
        for j in range(0,i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] > max_len:
            max_len = dp[i]
    return max_len

# Top down memoization
def longest_increasing_subsequence_top_down(nums:List[int])->int:
    dp = [-1] * len(nums)
    def compute_lis(nums:List[int], n:int)->int:
        if dp[n] != -1: return dp[n]
        if n < 0:
            ans = 0
        elif n == 0:
            ans = 1
        else:
            ans = 1
            for j in range(n - 1,-1,-1):
                val = compute_lis(nums,j)
                if nums[i] > nums[j] and val + 1 > ans:
                    ans = val + 1
        dp[n] = ans
        return ans
    max_len = 1
    for i in range(0,len(nums)):
        v = compute_lis(nums,i)
        if v > max_len:
            max_len = v
    return max_len

# Recursive solution to longest increassing sub sequence
def longest_increasing_subseqeunce(nums:List[int])->int:
    def longest_increasing_subsequence_recursive(nums:List[int],n:int)->int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            ans = 1
            for j in range(n - 1,-1,-1):
                val = longest_increasing_subsequence_recursive(nums,j)
                if nums[j] < nums[n] and val + 1 > ans:
                    ans = val + 1
            return ans
    max_len = 1
    for i in range(0,len(nums)):
        v = longest_increasing_subsequence_recursive(nums,i)
        if v > max_len:
            max_len = v
    return max_len

print(longest_increasing_subsequence_top_down([50, 3, 10, 7, 40, 80, 11]))
print(longest_increasing_subseqeunce([50, 3, 10, 7, 40, 80, 11]))
print(longest_increasing_subsequence_bottom_up([50, 3, 10, 7, 40, 80, 11]))