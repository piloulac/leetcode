# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            dictionary.setdefault(num,0)
            dictionary[num] += 1
            
        return max(dictionary, key=dictionary.get)

    def majorityElement2(self, nums: List[int]) -> int:
        count_majority = len(nums)//2
        
        for num in set(nums):
            my_count = nums.count(num)
            if my_count>count_majority:
                return num