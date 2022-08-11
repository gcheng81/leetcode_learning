"https://leetcode.com/problems/average-of-levels-in-binary-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            total = 0
            for _ in range(size):
                cur = q.popleft()
                if cur:
                    total += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            avg = total / size
            res.append(avg)
        
        return res
        
