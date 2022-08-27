"https://leetcode.com/problems/combination-sum/"


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtracking(path, total, i):
            if total > target or i>=len(candidates):
                return
            
            if total == target:
                res.append(path.copy()) # path[:]
                return
            
            path.append(candidates[i])
            backtracking(path, total+candidates[i], i)
            path.pop()
            backtracking(path, total, i+1)
        
        if candidates:
            backtracking([], 0, 0)
        return res
