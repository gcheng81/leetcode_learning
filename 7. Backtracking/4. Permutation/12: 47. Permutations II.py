"https://leetcode.com/problems/permutations-ii/"

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        def dfs():
            if len(path)==len(nums):
                res.append(path[:])
                return
            
            for i in count:
                if count[i]>0:
                    path.append(i)
                    count[i] -= 1
                    dfs()
                    path.pop()
                    count[i] += 1
        
        dfs()
        return res
        
