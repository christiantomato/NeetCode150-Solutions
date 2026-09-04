"""
1. Two Sum
09/03/26

Approach:
Brute force by checking sums. Ignore redundant sums and compute
only the following. 

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        #loop through list
        for i in range(len(nums)):
            #test sums with only the following numbers 
            for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target: return [i, j]
        
        