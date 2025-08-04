# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root):

            if not root:
                return True, -1, -1

            if not root.left and not root.right:
                return True, root.val, root.val

            elif not root.left:
                A = root.val < root.right.val
                B, v1, v2 = isValid(root.right)
                C = root.val < v1
                return A and B and C, root.val, v2
            elif not root.right:
                A = root.val > root.left.val
                B, v1, v2 = isValid(root.left)
                C = root.val > v2
                return A and B and C, v1, root.val
            else:
                # both nodes exist
                A = root.val > root.left.val and root.val < root.right.val
                Bl, v1l, v2l = isValid(root.left)
                Br, v1r, v2r = isValid(root.right)
                C = v2l < root.val and root.val < v1r
                return A and Bl and Br and C, v1l, v2r

        out, _, _ = isValid(root)

        return out

