"https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/"
"https://stackoverflow.com/questions/69799320/meaning-of-stack-10-in-python"

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()
        
        return "".join([c*n for c, n in stack])

# s[-1] return last element from list(s): [char, num_count]
# stack[-1] = the top element in stack = the last element in stack list
# s[-1][0] means first element of the last item in s: char
# s[-1][1] means second element of the last item in s: num_count
