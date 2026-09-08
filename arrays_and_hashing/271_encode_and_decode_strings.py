"""
1. Top k Frequent Elements
09/08/26

Approach:
Used hint, using a length based prefix as a delimeter to encode and decode. 

Time Complexity: O(k^2), O(n)
Space Complexity: O(n + k), O(n + k)
"""

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""

        #use a length based prefix
        for string in strs:
            encoded_string = encoded_string + str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_strings = []

        #decode using the prefix
        i = 0
        while i < len(s):
            #get length
            j = s.find('#', i)
            length = int(s[i:j])
            #skip over separator
            i = j + 1
            #get the string
            clipped_str = s[i : i + length]
            #add to list
            decoded_strings.append(clipped_str)
            #go to next 
            i += length

        return decoded_strings
