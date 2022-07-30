"https://leetcode.com/problems/3sum-closest/"

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            l = i + 1
            r = n - 1
            while (l < r):
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        
        return target - diff
