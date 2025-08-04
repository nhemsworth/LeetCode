# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        node_list = [root]
        val_list = []

        while node_list:
            lvl_list = []
            next_node_list = []
            for node in node_list:
                lvl_list.append(node.val)
                if node.left:
                    next_node_list.append(node.left)
                if node.right:
                    next_node_list.append(node.right)

            val_list.append(lvl_list)
            node_list = next_node_list

        return val_list

