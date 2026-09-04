"""
242. Valid Anagram
09/02/26

Approach:
Keep track of frequency using a hash dictionary where the key is the letter, 
and the data is the frequency. Serendipitously, Python has a library for this.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use the built in frequency map
        return Counter(s) == Counter(t)
        