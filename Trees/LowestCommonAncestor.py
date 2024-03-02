
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root
        while curr:
            if (p.val < curr.val and q.val < curr.val):
                curr = curr.left
            elif (curr.val < p.val and curr.val < q.val):
                curr = curr.right
            else:
                return curr
