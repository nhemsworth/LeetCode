"""
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
linked list sorted as well.

Beats 72.54% on execution speed.
Beats 11.20% on memory usage.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        prev_node = node = head
        node = node.next

        while node:

            if node.val == prev_node.val:
                prev_node.next = node.next
            else:
                prev_node = node
            node = node.next

        return head
