"""
1. Group Anagrams
09/05/26

Approach:
Group together anagrams in a hash dictionary using the frequency map as the hash key.

Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #create a hash dictionary, keys: hashable frequency counter, data: list holding all the anagram strings
        anagrams = {}

        #loop through list of strings
        for string in strs:
            frequency_table = [0] * 26
            #build frequency table
            for char in string:
                #add each letter frequency
                frequency_table[ord(char) - 97] += 1
            #turn immutable so it can be hashable
            hashable_frequency_table = tuple(frequency_table)

            if hashable_frequency_table in anagrams:
                #group together the anagram strings
                anagrams[hashable_frequency_table].append(string)
            else:
                #add new key
                anagrams[hashable_frequency_table] = [string]

        #return the grouped anagrams
        return list(anagrams.values())

