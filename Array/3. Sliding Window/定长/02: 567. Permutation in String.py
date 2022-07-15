"https://leetcode.com/problems/permutation-in-string/"
# 比28多一步

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        
        for end in range(len(s1)-1, len(s2)):
            if Counter(s2[start:end+1]) == Counter(s1):
                return True
            start += 1
        return False
        
