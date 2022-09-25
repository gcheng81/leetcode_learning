"https://leetcode.com/problems/reverse-words-in-a-string/"

# Both solutions: TC = O(N), SC = O(N)

# Solution 1: Two Pointers
class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = self.remove_useless_space(s)
        str_list = str_list[::-1]
        
        slow = 0
        for fast in range(len(str_list)):
            if str_list[fast] == ' ':
                str_list[slow:fast] = str_list[slow:fast][::-1]
                slow = fast+1
        str_list[slow:] = str_list[slow:][::-1]
        
        return "".join(str_list)
    
    def remove_useless_space(self, s):
        left = 0
        right = len(s)-1
        
        while left<=right and s[left]==' ':
            left += 1
        while left<=right and s[right]==' ':
            right -= 1
        
        res = []
        while left<=right:
            if s[left] != ' ':
                res.append(s[left])
            else:
                if res[-1] != ' ':
                    res.append(s[left])
            left += 1
        return res

# Solution 2: Built-in functions
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()[::-1]
        return ' '.join(words)
        
