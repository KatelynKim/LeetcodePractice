# Recursive inorder traversal using dfs
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    res = []
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res[k-1]

# Iterative inorder traversal using stack
# (https://www.educative.io/answers/how-to-perform-an-iterative-inorder-traversal-of-a-binary-tree)
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root
    n = 0
    # while stack is not empty or curr is not None.
    # If stack is not empty but curr is None, this means curr is at a leaf node, so we want to pop from a stack.
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        n += 1
        if (n == k):
            return curr.val

        # this could be None, in which case we resume popping from the stack
        curr = curr.right
