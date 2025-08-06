# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findkthSmallest(node: Optional[TreeNode], k: int):

            """
            Returns either the kth smallest or the number of smallest nodes that were traversed
            """

            if not node:
                return None, k
            elif k == 1 and not node.left:
                return node, 0
            else:
                n_l, k_l = findkthSmallest(node.left, k)
                if n_l:
                    return n_l, 0
                if k_l == 1:
                    return node, 0
                n_r, k_r = findkthSmallest(node.right, k_l - 1)
                if n_r:
                    return n_r, 0
                else:
                    return None, k_r

        n, kl = findkthSmallest(root, k)

        return n.val


