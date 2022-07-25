"https://leetcode.com/problems/ransom-note/"

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        m_dict = {}
        m_dict = Counter(magazine)
        
        for r in ransomNote:
            if r not in m_dict:
                return False
            else:
                m_dict[r] -= 1
        
        for v in m_dict.values():
            if v<0:
                return False
        
        return True
