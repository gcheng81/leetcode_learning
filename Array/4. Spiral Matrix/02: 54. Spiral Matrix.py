"https://leetcode.com/problems/spiral-matrix/"

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        
        left = up = 0
        right = col-1
        down = row-1
        
        while left<=right and up<=down:
            # ->
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            
            # up->down
            for j in range(up, down+1):
                res.append(matrix[j][right])
            right -= 1
            
            # necessary
            if not (left<=right and up<=down):
                break
            
            # <-
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            
            # down->up
            for j in range(down, up-1, -1):
                res.append(matrix[j][left])
            left += 1
        return res
    
