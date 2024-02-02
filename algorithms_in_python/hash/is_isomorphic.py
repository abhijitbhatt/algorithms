# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150

import unittest
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        reverse_lookup = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
                if t[i] in reverse_lookup:
                    return False
                reverse_lookup[t[i]] = s[i]
            else:
                if lookup[s[i]] != t[i] or reverse_lookup[t[i]] != s[i]:
                    return False
        return True

class TestIsomorphic(unittest.TestCase):
    def test_repeating_char(self):
        assert Solution().isIsomorphic('paper','title')
    def test_multiple_char_mapping_to_one(self):
        assert not Solution().isIsomorphic('foo','bar')
