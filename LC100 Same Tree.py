from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (not p and q) or (p and not q):
            return False
        elif (not p and not q):
            return True

        if p.val != q.val:
            return False

        p_list = [p]
        q_list = [q]

        while p_list and q_list:
            next_p_list = []
            next_q_list = []

            next_p_val_list = []
            next_q_val_list = []

            for entry in p_list:
                if entry.left:
                    next_p_list.append(entry.left)
                    next_p_val_list.append(entry.left.val)
                else:
                    next_p_val_list.append(None)
                if entry.right:
                    next_p_list.append(entry.right)
                    next_p_val_list.append(entry.right.val)
                else:
                    next_p_val_list.append(None)
            for entry in q_list:
                if entry.left:
                    next_q_list.append(entry.left)
                    next_q_val_list.append(entry.left.val)
                else:
                    next_q_val_list.append(None)
                if entry.right:
                    next_q_list.append(entry.right)
                    next_q_val_list.append(entry.right.val)
                else:
                    next_q_val_list.append(None)

            if next_p_val_list != next_q_val_list:
                return False

            p_list = next_p_list
            q_list = next_q_list

        return len(p_list) == len(q_list)