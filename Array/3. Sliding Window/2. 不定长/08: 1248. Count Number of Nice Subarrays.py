"https://leetcode.com/problems/count-number-of-nice-subarrays/"

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def leqK(nums, k):
            start = 0
            count_odd = 0
            count = 0
            
            for end in range(len(nums)):
                if nums[end]%2 == 1:
                    count_odd += 1
                
                while count_odd > k:
                    if nums[start]%2 == 1:
                        count_odd -= 1
                    start += 1
                count += end-start+1
            return count
        return leqK(nums, k) - leqK(nums, k-1)
