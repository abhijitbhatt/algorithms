# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
# The problem is poorly worded. Read the discussion to understand the logic
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lookup = {}
        reverse_lookup = {}
        i = 0
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for i,w in enumerate(words):
            if w not in lookup:
                lookup[w] = pattern[i]
                if pattern[i] in reverse_lookup:
                    return False
                else:
                    reverse_lookup[pattern[i]] = w
            else:
                if lookup[w] != pattern[i] or reverse_lookup[pattern[i]] != w:
                    return False
        return True

print(Solution().wordPattern('abba','dog cat cat fish'))