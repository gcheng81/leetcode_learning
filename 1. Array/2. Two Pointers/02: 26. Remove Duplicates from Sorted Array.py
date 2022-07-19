"https://leetcode.com/problems/remove-duplicates-from-sorted-array/"

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        slow=0
        for fast in range(1, len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            
        return slow+1
