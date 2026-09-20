"""
128. Longest Consecutive Sequence
09/20/26

Approach:
Convert list to set and then identify possible starts of a sequence. Continue to use the set
for O(1) lookups for the +1 element. 

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #convert the array to a hash set
        nums_set = set(nums)
        longest = 0

        #loop through unique numbers and consider possible sequence starts
        for num in nums_set: 
            #check if num - 1 exists
            if num-1 not in nums_set:
                current = num
                streak = 1

                #count sequence
                while current + 1 in nums_set:
                    current += 1
                    streak += 1

                #update longest
                if streak > longest: longest = streak

        return longest
            