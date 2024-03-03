class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs (node, left, right):
            if not node:
                return True

            if node.val >= right or node.val <= left:
                return False

            else:
                return dfs(node.right, node.val, right) and dfs(node.left, left, node.val)


        return dfs(root, -inf, inf)