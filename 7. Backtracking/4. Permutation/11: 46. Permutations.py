"https://leetcode.com/problems/permutations/"

# 排列问题的不同:
# - 每层都是从0开始搜索而不是startIndex
# - 需要记录path里已经放了哪些元素

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(res, path, nums):
            if len(path) == len(nums): # collect all leaf nodes
                res.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(res, path, nums)
                path.pop()
            
        res = []
        path = []
        dfs(res, path, nums)
        return res
            
            
