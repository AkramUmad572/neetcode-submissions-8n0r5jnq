# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter, self.ans = 0, 0

        def dfs(node: 'Node') -> int:
            if not node:
                return None
            dfs(node.left)

            self.counter += 1
            if self.counter == k:
                self.ans = node.val
            dfs(node.right)
        
        dfs(root)
        return self.ans