"https://leetcode.com/problems/maximum-depth-of-binary-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: DFS
# Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        max_depth = 1 + max(left_depth, right_depth)
        return max_depth

    
# Solution 2: BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        count = 0
        #res = []
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
                #res.append(level)
                count += 1
        return count
        #return len(res)
        
