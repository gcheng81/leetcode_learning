"https://leetcode.com/problems/spiral-matrix-ii/"

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        left = up = 0
        right = down = n-1
        num = 1
        
        while left<=right and up<=down:
            # ->
            for col in range(left, right+1):
                matrix[up][col] = num
                num += 1
            up += 1
            
            # up->down
            for row in range(up, down+1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            if not (left<=right and up<=down):
                break
            
            # <-
            for col in range(right, left-1, -1):
                matrix[down][col] = num
                num += 1
            down -= 1
            
            # down->up
            for row in range(down, up-1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
        
        return matrix
      
