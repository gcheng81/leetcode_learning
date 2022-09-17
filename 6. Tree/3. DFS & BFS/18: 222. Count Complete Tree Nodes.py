"https://leetcode.com/problems/count-complete-tree-nodes/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: DFS
# Recursion
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_nodes = self.countNodes(root.left)
        right_nodes = self.countNodes(root.right)
        return 1+left_nodes+right_nodes

    
# Solution 2: BFS
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        #level = []
        count = 0
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur:
                    #level.append(cur)
                    count += 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return count
        
