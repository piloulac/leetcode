# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        max_all_time = -sys.maxsize - 1
        
        for num in nums:
            curr_max += num
            max_all_time = max(max_all_time, curr_max)
            
            if curr_max<0:
                curr_max = 0

        return max_all_time