"https://leetcode.com/problems/binary-subarrays-with-sum/"

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def leqG(nums, goal):
            if goal<0: # 必须要有，不然runtime error。因为goal>=0，会取到0
                return 0
            
            start = 0
            count_one = 0
            count = 0
            for end in range(len(nums)):
                if nums[end] == 1:
                    count_one += 1
                
                while count_one > goal:
                    if nums[start] == 1:
                        count_one -= 1
                    start+=1
                count += end-start+1
            return count
        return leqG(nums, goal) - leqG(nums, goal-1)
