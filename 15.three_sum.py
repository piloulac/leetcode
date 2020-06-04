# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.


# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4], 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        if all(i == 0 for i in nums):
            return [[0,0,0]]
        
        result = set()
        
        nums.sort()
        
        for i in range(len(nums)):
            left = i + 1 
            right = len(nums)-1
            
            while left < right:
                sums = nums[left] + nums[right]
                
                if sums + nums[i] == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                if sums + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
                    
        
        return result