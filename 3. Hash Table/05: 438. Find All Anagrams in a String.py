"https://leetcode.com/problems/find-all-anagrams-in-a-string/"

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # corner case
        if len(p) > len(s):
            return []
        
        start = 0
        #initialize sCount and pCount hashmaps
        pCount = {}
        sCount = {}
        for i in range(len(p)):
			pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        # first compare the first sub-string of s
        ans = [0] if sCount == pCount else []
        
        # start from the second sub-string of s
        for end in range(len(p), len(s)):
            # update map
            sCount[s[end]] = 1 + sCount.get(s[end], 0)
            # remove start from hashmap
            sCount[s[start]] -= 1
            if sCount[s[start]] == 0:
                sCount.pop(s[start])
            # update start pointer
            start += 1
            
            if sCount == pCount:
                ans.append(start)
        return ans
    
# dictionary.get(keyname, value)
    # keyname: Required. The keyname of the item you want to return the value from
    # value: Optional. A value to return if the specified key does not exist.
