"https://leetcode.com/problems/fruit-into-baskets/"

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_len = float('-inf')
        adict = {}
        
        for end in range(len(fruits)):
            # add fruit
            if fruits[end] in adict:
                adict[fruits[end]] += 1
            else:
                adict[fruits[end]] = 1
            
            # move window
            while len(adict)>2:
                adict[fruits[start]] -= 1 # move content
                if adict[fruits[start]] == 0:
                    del adict[fruits[start]]
                start += 1 # move border
            
            max_len = max(max_len, end-start+1)
        
        return 0 if max_len==float('-inf') else max_len
