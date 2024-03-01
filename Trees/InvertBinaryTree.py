class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            node.left = right
            node.right = left
            return node


        return dfs(root)
