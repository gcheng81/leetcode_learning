"https://leetcode.com/problems/combination-sum-ii/"

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtracking(start_index, target, path):
            if target < 0:
                return
            
            if target == 0:
                res.append(path.copy())
                return
            
            prev = -1    
            for i in range(start_index, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                path.append(candidates[i])
                backtracking(i+1, target-candidates[i], path)
                path.pop()
                prev = candidates[i]
        
        if candidates:
            backtracking(0, target, [])
        return res
