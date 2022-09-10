"https://leetcode.com/problems/minimum-depth-of-binary-tree/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Soluton 1: BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        q = collections.deque()
        if root:
            q.append(root)
            depth = 1
        else:
            return 0
        
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
            
 # Solution 2: DFS           
    
