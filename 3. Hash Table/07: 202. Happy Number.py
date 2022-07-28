"https://leetcode.com/problems/happy-number/"

# Solution 1: Detect Cycles with a HashSet
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_sum(num):
            total = 0
            while num: # num = 82
                total += (num % 10) ** 2 # Get 2^2
                num = num // 10 # Get 8
            return total
        
        record = set()
        while n != 1:
            n = calculate_sum(n)
            if n in record:
                return False
            else:
                record.add(n)
        return True

# Solution 2: Floyd's Cycle-Finding Algorithm
