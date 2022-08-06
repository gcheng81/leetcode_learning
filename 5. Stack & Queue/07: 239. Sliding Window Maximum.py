"https://leetcode.com/problems/sliding-window-maximum/"

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # contain index
        
        if len(nums)==0 or k>len(nums):
            return []
        
        left = 0
        for right in range(len(nums)):
            while q and nums[q[-1]]<nums[right]: # in descending order
                q.pop()
            q.append(right)
            
            if left>q[0]: # q[0] is index, range(0, len(nums))
                q.popleft()
            
            if (right+1) >= k:
                res.append(nums[q[0]]) # q[0] must be the index of max value
                left += 1
        
        return res
            
