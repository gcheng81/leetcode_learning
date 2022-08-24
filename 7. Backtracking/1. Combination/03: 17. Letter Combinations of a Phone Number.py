"https://leetcode.com/problems/letter-combinations-of-a-phone-number/"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtracking(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            
            for ch in letterMap[digits[i]]: # 横向遍历 同一层
                backtracking(i+1, cur_str+ch) # 纵向遍历 下一层
        
        if digits:
            backtracking(0, "")
        return res
           
