"https://leetcode.com/problems/increasing-subsequences/"

# Solution 1: 用 set 去重
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0 or len(nums)>15:
            return []
        
        def dfs(start_index, res, path, nums):
            if len(path)>=2:
                res.add(tuple(path))
            if start_index == len(nums):
                return
            
            last = path[-1] if path else -200
            for i in range(start_index, len(nums)):
                if nums[i] >= last:
                    path.append(nums[i])
                    dfs(i+1, res, path, nums)
                    path.pop()
             
        res = set()
        path = []
        dfs(0, res, path, nums)
        return res
      
      
# Solution 2: 不用 set 去重 => 多一个 array
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0 or len(nums)>15:
            return []
        
        def dfs(start_index, res, path, nums):
            if len(path)>=2:
                res.append(tuple(path))
            if start_index == len(nums):
                return
            
            last = path[-1] if path else -200
            used = []
            for i in range(start_index, len(nums)):
                if nums[i] in used:
                    continue
                if nums[i] >= last:
                    path.append(nums[i])
                    dfs(i+1, res, path, nums)
                    path.pop()
                used.append(nums[i])
                
        res = []
        path = []
        dfs(0, res, path, nums)
        return res
