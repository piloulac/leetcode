# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
# [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        reversed_number = 0
        is_negative = False

        if x >= 2**31-1 or x <= -2**31: 
            return 0
        
        if x<0:
            is_negative = True
            x = abs(x)
        
        while x > 0:
            reversed_number = (reversed_number*10) + (x % 10)
            x //= 10
        
        if reversed_number >= 2**31-1 or reversed_number <= -2**31: 
            return 0

        return reversed_number * (1 if not is_negative else -1)
        