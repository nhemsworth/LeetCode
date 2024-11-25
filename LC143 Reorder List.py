"""
143. Reorder List

Beats 65.34% on execution time
Beats 86.43% on memory usage
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node_list = []
        node = head

        # Populate node_list with all nodes in sequence
        while node:
            node_list.append(node)
            node = node.next

        # Initialize pointers
        i = 0
        j = len(node_list) - 1

        while i < j:
            node_list[i].next = node_list[j]
            if j == i + 1:
                node_list[j].next = None
            else:
                node_list[j].next = node_list[i + 1]
            i += 1
            j -= 1

        if i == j:
            node_list[i].next = None

        return