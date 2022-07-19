"https://leetcode.com/problems/valid-perfect-square/"

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left = 1
        right = num // 2
        
        while left <= right:
            mid = (left+right)//2
            mlt = mid ** 2
            if mlt > num:
                right = mid - 1
            elif mlt < num:
                left = mid + 1
            else:
                return True
        return False
        
