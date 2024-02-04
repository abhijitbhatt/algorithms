from typing import List

def coin_change_bottom_up(total:int, coins:List[int])->int:
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for t in range(1, total + 1):
        for coin in coins:
            if total - coin >= 0:
                dp[t] = min(dp[t],dp[t - coin] + 1)
    return dp[-1]

def coin_change_top_down(total:int, coins:List[int])->int:
    dp = [-1] * (total + 1)
    dp[0] = 0
    def calculate(total:int, coins:List[int])->int:
        if dp[total] != -1:
            return dp[total]
        elif total == 0:
            return 0
        else:
            result = float('inf')
            for coin in coins:
                if total - coin >= 0:
                    val = calculate(total - coin,coins) + 1
                    if val < result:
                        result = val
            dp[total] = result
            return dp[total]
    result = calculate(total,coins)
    if result == float('inf'):
        return -1
    else:
        return result

def coin_change(total:int, coins:List[int])->int:
    def coin_change_recursive(total:int, coins:List[int])->int:
        if total == 0:
            return 0
        else:
            result = float('inf')
            for coin in coins:
                if total - coin >= 0:
                    val = coin_change_recursive(total - coin,coins) + 1
                    if val < result:
                        result = val
            return result
    result = coin_change_recursive(total, coins)
    if result == float('inf'):
        return -1
    else:
        return result

print(coin_change(11,[1,3,5]))
print(coin_change_top_down(11,[1,3,5]))
print(coin_change_bottom_up(11,[1,3,5]))