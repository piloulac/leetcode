# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        return xStr == xStr[::-1]

# Next challenges:
# do it without converting to string