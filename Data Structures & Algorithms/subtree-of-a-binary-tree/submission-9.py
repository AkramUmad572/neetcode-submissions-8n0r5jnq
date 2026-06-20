# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val == subRoot.val:
                return same_tree(root.left, subRoot.left) and same_tree(root.right, subRoot.right)
            else:
                return False
        if not root:
            return False
        elif root.val == subRoot.val:
            return same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        
        

        
