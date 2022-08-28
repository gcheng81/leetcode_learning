"https://leetcode.com/problems/restore-ip-addresses/"


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(startIndex, path, res, s):
            if startIndex == len(s) and len(path)==4:
                res.append('.'.join(path))
                return
                
            for i in range(startIndex, len(s)):
                tmp = s[startIndex:i+1]
                if int(tmp)>=0 and int(tmp)<=255:
                    if tmp.startswith('0') and len(tmp)!=1: # 000, 024
                        continue
                    else:
                        path.append(tmp)
                        dfs(i+1, path, res, s)
                        path.pop()
             
        res = []
        path = []
        startIndex = 0
        dfs(startIndex, path, res, s)
        return res
