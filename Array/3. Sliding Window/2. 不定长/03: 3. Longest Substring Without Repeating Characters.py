"https://leetcode.com/problems/longest-substring-without-repeating-characters/"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = float('-inf')
        start = 0
        mark = set()
        
        for end in range(len(s)):
            while s[end] in mark:
                mark.remove(s[start])#注意remove的是s[start]而不是s[end]
                start+=1
            max_len = max(max_len, end-start+1)
            mark.add(s[end])#s[end] not in mark
        return 0 if max_len==float('-inf') else max_len
