"https://leetcode.com/problems/combination-sum-iii/"

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.backtracking(k, n, 1, res, path, 0)
        return res
    
    def backtracking(self, k, n, start_index, res, path, total):
        if total > n:
            return
        
        if len(path) == k:
            if total == n:
                res.append(path[:])
            return
        
        for i in range(start_index, 10):
            total += i
            path.append(i)
            self.backtracking(k, n, i+1, res, path, total)
            total -= i
            path.pop()

        
