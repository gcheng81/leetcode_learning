"https://leetcode.com/problems/4sum/"

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n<4:
            return []
        nums.sort()
        res = []
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:continue  #去重i
            
            for j in range(i+1, n):
                if j>i+1 and nums[j]==nums[j-1]:continue  #去重j
                
                l = j+1
                r = n-1       
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l+1<r and nums[l]==nums[l+1]: l+=1    #去重l
                        while r-1>l and nums[r]==nums[r-1]: r-=1    #去重r
                        l+=1
                        r-=1
                    elif total<target:
                        l+=1
                    else:
                        r-=1
        return res
