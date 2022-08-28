"https://leetcode.com/problems/palindrome-partitioning/"


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s==None:
            return []
        
        def dfs(s, start_index, path, res):
            if start_index == len(s):
                res.append(path.copy())
                return
                
            for i in range(start_index, len(s)):
                if s[start_index:i+1] == s[start_index:i+1][::-1]:
                    path.append(s[start_index:i+1])
                    dfs(s, i+1, path, res)
                    path.pop()
        
        start_index = 0
        path = []
        res = []
        dfs(s, start_index, path, res)
        return res
        
