# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        nums.sort()
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            
            while start < end:
                sums = nums[i] + nums[start] + nums[end]

                if closest is None or abs(target - sums) < abs(target - closest):
                    closest = sums

                if sums>target:
                    end -= 1
                else:
                    start += 1
                    
        return closest