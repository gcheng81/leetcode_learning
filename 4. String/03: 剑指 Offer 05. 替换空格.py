"https://leetcode.cn/problems/ti-huan-kong-ge-lcof/"

# Solution: no extra space
# Notice:
# (1) how to use list.extend(iterable) function
# (2) how to add "%20": slice
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = list(s)
        front = len(s) - 1
        num_sp = res.count(" ")
        res.extend(" "* num_sp * 2) # 是加在最后
        back = len(res) - 1
        
        while front >= 0:
            if res[front] != " ":
                res[back] = res[front]
                back -= 1
            else:
                res[back-2: back+1] = "%20" # key point!!!
                back -= 3
            front -= 1
        
        return "".join(res)
        
        
