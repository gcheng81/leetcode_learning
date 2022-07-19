"https://leetcode.com/problems/max-consecutive-ones-iii/"

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_num_1 = float('-inf')
        start = 0
        count_one = 0
        count_zero = 0
        
        for end in range(len(nums)):
            if nums[end] == 1:
                count_one += 1
            else:
                count_zero += 1
            
            while count_zero > k:
                if nums[start] == 1:
                    count_one -= 1
                else:
                    count_zero -= 1
                start += 1
            max_num_1 = max(max_num_1, end-start+1)
        
        return 0 if max_num_1==float('-inf') else max_num_1
