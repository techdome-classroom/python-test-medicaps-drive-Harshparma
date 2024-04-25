
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        mappings = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mappings:
                top_element = stack.pop() if stack else '#'
                
                if mappings[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
