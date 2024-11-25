"""
19. Remove Nth Node from End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Beats 91.67% on execution time
Beats 45.49% on memory usage
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        node = head
        node_list = []

        # Populate node_list with all nodes in sequence
        while node:
            node_list.append(node)
            node = node.next

        # If only one node is present, we return None
        if len(node_list) == 1:
            return None
        # If we're removing the last element, we need to set the pointer to None
        elif n == 1:
            prev_node = node_list[-n - 1]
            prev_node.next = None
        # If we're removing the first element, the head needs to point to the next element
        elif n == len(node_list):
            head = head.next
        # General case: previous node points to next node
        else:
            prev_node = node_list[-n - 1]
            next_node = node_list[-n + 1]
            prev_node.next = next_node
        return head