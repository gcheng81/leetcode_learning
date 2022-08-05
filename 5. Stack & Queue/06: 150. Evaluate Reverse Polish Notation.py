"https://leetcode.com/problems/evaluate-reverse-polish-notation/"

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(int(item))
            else:
                first_element = stack.pop()
                second_element = stack.pop()
                if item == "+":
                    res = first_element + second_element
                elif item == "-":
                    res = second_element - first_element
                elif item == "*":
                    res = first_element * second_element
                elif item == "/":
                    res = int(second_element / first_element)
                stack.append(res)
        return stack.pop()      
