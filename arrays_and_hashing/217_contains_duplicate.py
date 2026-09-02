"""
217. Contains Duplicate

Approach:
Loop through array once, keep track of encountered numbers 
and return false if duplicate is found.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()

        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else: return True
        return False 
