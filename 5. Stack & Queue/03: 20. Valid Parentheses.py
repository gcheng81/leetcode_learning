"https://leetcode.com/problems/valid-parentheses/"

# Solution 1:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                
                if char == ")":
                    if top != "(":
                        return False
                
                elif char == "]":
                    if top != "[":
                        return False
                
                elif char == "}":
                    if top != "{":
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
