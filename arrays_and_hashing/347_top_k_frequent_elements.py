"""
1. Top k Frequent Elements
09/07/26

Approach:
Use hash dictionary for frequencies, then sort using most_common() which uses a min heap. 

Time Complexity: O(n * log(k))
Space Complexity: O(n)
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #use counter to get frequencies
        num_frequencies = Counter(nums)
        #use most common method to get top k, and just return the number
        return [num for num, freq in num_frequencies.most_common(k)]


            

        