"https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/"

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if len(stack)==0:
                stack.append(char)
            else:
                top = stack.pop()
                if char != top:
                    stack.append(top)
                    stack.append(char)
        
        return ''.join(stack)
 
# More Simple
 class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        
