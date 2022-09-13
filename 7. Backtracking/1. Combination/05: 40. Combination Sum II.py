"https://leetcode.com/problems/combination-sum-ii/"

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        start_index = 0
        total = 0
        self.backtracking(res, path, start_index, candidates, target, total)
        return res
        
    def backtracking(self, res, path, start_index, nums, target, total):
        if total > target:
            return
        
        elif total == target:
            res.append(path[:])
            return
        
        else:
            for i in range(start_index, len(nums)):
                if i>start_index and nums[i-1] == nums[i]:
                    continue
            
                path.append(nums[i])
                total += nums[i]
                self.backtracking(res, path, i+1, nums, target, total)
                path.pop()
                total -= nums[i]
