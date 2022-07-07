"https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"

# Solution: Use Binary Search to find the left and right border respectively.
# Ref: https://www.bilibili.com/video/BV1wy4y1k76F?spm_id_from=333.337.search-card.all.click&vd_source=1280166b4488c3620a50861f6d3d9078

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeftBorder():
            left = 0
            right = len(nums)-1
            
            while left<=right:
                mid = (left+right)//2
                
                if nums[mid]>target:
                    right = mid-1
                    
                elif nums[mid]<target:
                    left = mid+1
                else:
                    if mid==0 or nums[mid-1]<target:
                        return mid
                    else:
                        right = mid-1
            return -1
        
        def searchRightBorder():
            left = 0
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]>target:
                    right = mid-1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    if mid==len(nums)-1 or nums[mid+1]>target:
                        return mid
                    else:
                        left = mid+1
            return -1
        
        return [searchLeftBorder(), searchRightBorder()]     
        
