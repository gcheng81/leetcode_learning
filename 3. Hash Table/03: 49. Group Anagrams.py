"https://leetcode.com/problems/group-anagrams/"

# Solution 1: key is Sorted String
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s)) # list -> string
            #key = tuple(sorted(s)) # list -> tuple
            ans[key].append(s)
            
        return ans.values()

# Solution 2: key is Count
