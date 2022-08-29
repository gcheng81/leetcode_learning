"https://leetcode.com/problems/subsets-ii/"

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(start_index, res, path, nums):
            res.append(path[:])
            if start_index >= len(nums):
                return
            
            for i in range(start_index, len(nums)):
                if i>start_index and nums[i]==nums[i-1]: # 去重必备2
                    continue
                path.append(nums[i])
                dfs(i+1, res, path, nums)
                path.pop()
        
        nums.sort() # 去重必备1
        res = []
        path = []
        dfs(0, res, path, nums)
        return res
