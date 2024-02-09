def permutation(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [nums[0]]
    else:
        results = []
        for x in permutation(nums[1:]):
            temp = str(x)
            for i in range(len(temp) + 1):
                results.append(int(temp[:i] + str(nums[0]) + temp[i:]))
        return results

print(permutation([1,2,3]))