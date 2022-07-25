"https://leetcode.com/problems/valid-anagram/"

# Solution 1: Dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def str_to_dict(string):
            adict = {}
            for i in string:
                if i in adict:
                    adict[i] += 1
                else:
                    adict[i] = 1
            return adict
        
        if len(s) != len(t):
            return False
        
        if str_to_dict(s) == str_to_dict(t):
            return True
        else:
            return False
         
# Using built-in function
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if Counter(s) == Counter(t):
            return True
        else:
            return False

          
# Solution 2: Array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        record = [0]*26
        
        for i in s:
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        
        for i in range(26):
            if record[i] != 0:
                return False
        
        return True   
