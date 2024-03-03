def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        queue.append(root)
        res = []
        while queue:
            qLen = len(queue)
            inner = []

            for i in range(qLen):
                node = queue.popleft()
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                inner.append(node.val)

            if inner:
                res.append(inner)

        return res