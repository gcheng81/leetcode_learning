"https://leetcode.com/problems/binary-tree-right-side-view/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
                    
