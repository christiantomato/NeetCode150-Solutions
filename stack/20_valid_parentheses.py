"""
20. Valid Parentheses
09/22/26

Approach:
Push L parens onto the stack and match them to their R paren.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        #def not valid if odd length
        if len(s) % 2 != 0: return False

        bracket_map = {
        '(': ')',
        '{': '}',
        '[': ']'
        }
    
        stack = []

        for str in s:
            if str == '(' or str == '{' or str == '[':
                #push it onto the stack
                stack.append(str)
                continue
            else:
                #cant have a closing with no open
                if(len(stack) == 0): return False
                #check if it matches the left bracket type on top of the stack
                if(bracket_map[stack.pop()] == str):
                    continue 
                else: return False

        #make sure everything got paired
        return len(stack) == 0
