"https://leetcode.com/problems/minimum-size-subarray-sum/"

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        total=0
        min_len=float('inf') # 取min所以设为正无穷
        
        for end in range(0, len(nums)):
            total += nums[end]
            
            while total>=target:
                min_len = min(min_len, end-start+1) # 必须先更新min_len，再更新start
                total -= nums[start]
                start += 1
        
        return 0 if min_len==float('inf') else min_len
