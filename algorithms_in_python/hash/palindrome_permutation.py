# Cracking coding interview - 6th edition problem 1.4
from collections import Counter
def palindrome_permutation(s:str):
    c = Counter(s)
    odd_count = 0
    for k,v in c.items():
        if v % 2 == 1:
            odd_count ++ 1
        if odd_count:
            return False
    return True


print(palindrome_permutation('carrace'))