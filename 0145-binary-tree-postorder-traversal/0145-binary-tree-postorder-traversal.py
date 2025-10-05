# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root,result):

            if not root:
                return 
            
            dfs(root.left,result)
            dfs(root.right,result)
            result.append(root.val)

        result=[]
        dfs(root,result)
        return result
        




        