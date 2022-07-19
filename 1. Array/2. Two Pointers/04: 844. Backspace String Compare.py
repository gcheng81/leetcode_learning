"https://leetcode.com/problems/backspace-string-compare/"

# Solution 1: Pointer
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removeHash(char):
            i=0
            while i<len(char):
                if char[i]=='#':
                    if i>0 and char[i-1] != "#":
                        char = char[:i-1] + char[i+1:]
                        i-=2 #delete "#" and the char before "#"
                    else:
                        char = char[i+1:]
                        i-=1 #delete only "#" 
                i+=1 # not else
            return char
                  
        return True if removeHash(s)==removeHash(t) else False

    
# Solution 2: Stack
