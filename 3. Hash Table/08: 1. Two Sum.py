"https://leetcode.com/problems/two-sum/"

# Solution 1: One-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for index in range(len(nums)):
            m = target - nums[index]
            if m not in record:
                record[nums[index]] = index
            else:
                return [record[m], index]
            
# Using enumerate()          
