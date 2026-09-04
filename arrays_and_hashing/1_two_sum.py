"""
1. Two Sum
09/04/26

Approach:
Keep track of differences in a hash dictionary which retains the indice, 
check if following numbers match a difference already computed.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #create a hash dictionary, keys: difference with target, data: indices
        differences = {}

        #loop through list
        for i in range(len(nums)):
            #check if current num is a computed difference
            if nums[i] in differences:
                #then nums[i] = target - nums[j], so retrieve index j which is stored
                return [differences[nums[i]], i]
            else:
                #otherwise add the difference to hash dictionary
                difference = target - nums[i]
                differences[difference] = i
