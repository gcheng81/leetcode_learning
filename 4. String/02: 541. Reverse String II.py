"https://leetcode.com/problems/reverse-string-ii/"

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_whole_string(string):
            l = 0
            r = len(string)-1
            while l<r:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
            return string
        
        s = list(s)
        for i in range(0, len(s), 2*k):
            left = i
            right = i+k
            s[left:right] = reverse_whole_string(s[left:right])
        
        return "".join(s)
            
        
