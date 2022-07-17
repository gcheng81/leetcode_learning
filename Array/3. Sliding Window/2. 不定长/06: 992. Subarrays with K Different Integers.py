"https://leetcode.com/problems/subarrays-with-k-different-integers/"

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def leqK(nums, k): # calculate <=k subarray
            start = 0
            adict = {}
            count = 0
        
            for end in range(len(nums)):
                if nums[end] not in adict:
                    adict[nums[end]] = 1
                else:
                    adict[nums[end]] += 1
            
                while len(adict) > k:
                    adict[nums[start]] -= 1 # content
                    if adict[nums[start]] == 0:
                        del adict[nums[start]]
                    start += 1 # border
                
                count += end-start+1
            return count
        
        return leqK(nums, k) - leqK(nums, k-1)
    # 2 subarray = <=2 subarrray - <=1 subarray
            
