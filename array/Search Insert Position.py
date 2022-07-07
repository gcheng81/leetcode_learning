"https://leetcode.com/problems/search-insert-position/"

"Solution 1: Brute Force (Optimization is in Notion)"
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1. front
        # 2. find in array
        # 3. in ???
        # 4. back
        
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        # 遍历完了数组，target比数组中的任何一个都大
        return len(nums)
      
"Solution 2: Binary Search"
"[left, right]"
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #[left, right]
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return right+1
  
