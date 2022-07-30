"https://leetcode.com/problems/3sum/"

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n<3:
            return []
        ans = []
        
        for i in range(n):
            left = i+1
            right = n-1
            
            if nums[i]>0: # [0, 1, 2, 3, ...]
                break
            if i>0 and nums[i]==nums[i-1]: #去重i：[有两个完全一样的值] or [0,0,0, ...]
                continue
            
            while left<right:
                total = nums[left]+nums[right]+nums[i]
                if total==0:
                    ans.append([nums[left], nums[right], nums[i]])
                    while left+1<right and nums[left]==nums[left+1]: #去重left
                        left += 1
                    while right-1>left and nums[right]==nums[right-1]: #去重right
                        right -= 1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return ans
