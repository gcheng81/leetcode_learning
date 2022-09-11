"https://leetcode.com/problems/binary-tree-right-side-view/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            #每次都取最后一个node
            node = q[-1] 
            res.append(node.val)
            
            size = len(q)
            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res
                 
        
# Solution 2: DFS-Recursion
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side = []
        
        def traverse(node, level): # level == index of the list
            if not node:
                return
            
            if level == len(right_side):
                right_side.append(node.val)
            traverse(node.right, level+1)
            traverse(node.left, level+1)
        
        traverse(root, 0)
        return right_side
