# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75
import unittest
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for e in s:
            if e == ']':
                tmp = ''
                while True:
                    x = stack.pop()
                    if x == '[':
                        repeat_count = ''
                        while len(stack) > 0 and stack[-1] >= '0' and stack[-1] <= '9':
                            n = stack.pop()
                            repeat_count = n + repeat_count
                        tmp = tmp * (1 if repeat_count == '' else int(repeat_count))
                        break
                    else:
                        tmp = x + tmp
                stack.extend(tmp)
            else:
                stack.append(e)
        return ''.join(stack)

class TestDecodeString(unittest.TestCase):
    def test_multiple_repititions(self):
        assert Solution().decodeString("2[abc]3[cd]ef") == 'abcabccdcdcdef'
    def test_nested_encoding(self):
        assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    def test_repeat_count_greater_than_10(self):
        assert Solution().decodeString("11[leetcode]") == "leetcode" * 11
