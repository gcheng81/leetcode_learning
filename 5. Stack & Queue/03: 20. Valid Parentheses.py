"https://leetcode.com/problems/valid-parentheses/"

# Solution 1: 左括号入栈
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
        

# Solution 2: 右括号入栈
# （1）一般方法
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == '(': 
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                if top != char:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False
            
           

# （2）优化：用字典
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        for char in s:
            if char in mapping:
                stack.append(mapping[char])
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if char != top:
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                
        
