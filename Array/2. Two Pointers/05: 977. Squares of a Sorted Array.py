“https://leetcode.com/problems/squares-of-a-sorted-array/”

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        res = [0] * len(nums) # 必须set新数组大小，否则会报错越界
        
        for i in range(len(nums)-1, -1, -1):
            square = 0;
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            res[i] = square ** 2
        return res
        
