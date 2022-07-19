"https://leetcode.com/problems/sqrtx/"

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        
        left = 1
        right = x//2
        
        while left<=right:
            mid = (left+right)//2
            mlt = mid ** 2
            if  mlt< x:
                left = mid + 1
            elif mlt > x:
                right = mid - 1
            else:
                return mid
        return right
