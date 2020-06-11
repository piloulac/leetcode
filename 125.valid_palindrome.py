# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        
        palindrome = True
        striped_s = re.findall('\w', s.lower())
        for i in range(len(striped_s)):
            if striped_s[i] != striped_s[len(striped_s)-1-i]:
                palindrome = False
                
        return palindrome