# https://atcoder.jp/contests/dp/tasks/dp_a
from typing import List

# Recursive solution is a good way to start formulating the solution using dynamic programming
# To come to kn-th stone the frog can jump from (n - 1)th stone or (n - 2)th stone
# Cost of coming from (n - 1)th stone to nth stone will be =
# Cost of coming to (n - 1) th stone + abs(height[n - 1] - height[n])
# Base conditions to terminate iterations
# Cost of coming to 0-th stone = 0 as the frog is there already
# Since we are ooking back up to 2 stones so there needs to another condition for n = 1
# The frong can come there only in one way
def min_cost_for_frog_recursive(n:int,height:List[int])->int:
    if n - 1 == 0:
        return 0
    elif n - 1 == 1:
        return abs(height[1] - height[0])
    else:
        cost_n_1_from_n_2 = abs(height[n - 1] - height[n - 2]) + min_cost_for_frog_recursive(n -1,height)
        cost_n_1_from_n_3 = abs(height[n - 1] - height[n - 3]) + min_cost_for_frog_recursive(n - 2,height)
        return min(cost_n_1_from_n_2,cost_n_1_from_n_3)

def min_cost_for_frog_dp_topdown(n:int,height:List[int])->int:
    dp = [-1] * n
    dp[0] = 0
    dp[1] = abs(height[1] - height[0])
    def min_cost_for_frog_topdown(n:int,height:List[int])->None:
        if dp[n-1] != -1:
            return dp[n - 1]
        cost_n_1_from_n_2 = abs(height[n - 1] - height[n - 2]) + min_cost_for_frog_topdown(n - 1,height)
        cost_n_1_from_n_3 = abs(height[n - 1] - height[n - 3]) + min_cost_for_frog_topdown(n - 2,height)
        dp[n - 1] = min(cost_n_1_from_n_2,cost_n_1_from_n_3)
        return dp[n - 1]
    min_cost_for_frog_topdown(n,height)
    return dp

print(min_cost_for_frog_dp_topdown(4,[10,30,40,20]))
