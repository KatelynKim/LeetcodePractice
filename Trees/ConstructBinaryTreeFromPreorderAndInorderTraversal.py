def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

    if not preorder or not inorder:
        return

    root = TreeNode(preorder[0])
    split = inorder.index(preorder[0])

    # why split + 1 when splicing preorder for the left root? Because we know based on inorder how many numbers there are in the left subtree (n = split).
    # For instance, if there were two numbers in the left subtree of the current root, then preorder should be spliced
    # from 1 (because we don't want to include the root) to split + 1 (as many nodes as "split" in the left subtree). + 1 is because
    # of exclusivity.
    root.left = self.buildTree(preorder[1:split+1], inorder[:split])
    root.right = self.buildTree(preorder[split+1:], inorder[split+1:])

    return root



