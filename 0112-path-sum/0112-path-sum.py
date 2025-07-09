class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:

        def dfs(root,current_sum):

            if root is None:
                return False
            current_sum += root.val
            if root.left is None and root.right is None:
                return current_sum == target
            

            return (dfs(root.left,current_sum) or dfs(root.right,current_sum))
        return dfs(root,0)