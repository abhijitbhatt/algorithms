# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
import unittest
def vowel_count(s:str)->int:
    return len([x for x in s if x in ['a','e','i','o','u']])

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = float('-inf')
        for i in range(0,len(s) - k + 1):
            if i == 0:
                vc = vowel_count(s[:k])
            else:
                if s[i - 1] in ['a','e','i','o','u']:
                    vc -= 1
                if s[i + k - 1] in ['a','e','i','o','u']:
                    vc += 1
            max_count = max(max_count, vc)
        return max_count

class TestMaxVowels(unittest.TestCase):
    def test_large_7(self):
        Solution().maxVowels('weallloveyou',7) == 4
