"https://leetcode.com/problems/combinations/"

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, res, 1, [])
        return res
        
    def backtracking(self, n, k, res, start_pos, path):
        if len(path) == k: # 终止条件
            res.append(path[:])
            return
        
        for i in range(start_pos, n+1):
            path.append(i)
            self.backtracking(n, k, res, i+1, path)
            path.pop()
        
        
# Optimization
for i in range(start_pos, n+1-(k-len(path))
# len(path): 已经选取的元素个数
# k-len(path): 还未选取的元素个数
# n+1-(k-len(path)): 还未选取的元素至多要从哪里开始搜索
