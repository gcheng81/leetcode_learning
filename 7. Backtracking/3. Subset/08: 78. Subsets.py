"https://leetcode.com/problems/subsets/"

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(start_index, res, path, nums):
            res.append(path.copy())
            if start_index >= len(nums):
                return
            
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                dfs(i+1, res, path, nums)
                path.pop()
        
        res = []
        path = []
        dfs(0, res, path, nums)
        return res
