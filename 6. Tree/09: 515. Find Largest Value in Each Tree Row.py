"https://leetcode.com/problems/find-largest-value-in-each-tree-row/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level:
                res.append(max(level))
        return res
