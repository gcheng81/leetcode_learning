"https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/"

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
        """
        res = list(s)
        res = res[n:len(res)] + res[0:n]
        return "".join(res)
        """
