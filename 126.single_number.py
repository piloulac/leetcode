# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
           dictionary.setdefault(num, 0)
            dictionary[num] += 1
        
        for key, value in dictionary.items():
            if value == 1:
                return key

    def singleNumber2(self, nums: List[int]) -> int:     
        return 2*sum(set(nums)) - sum(nums)