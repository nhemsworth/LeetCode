from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            head = node = list1
            list1 = list1.next
        else:
            head = node = list2
            list2 = list2.next

        while list1 or list2:
            if not list1:
                node.next = list2
                node = list2
                list2 = list2.next
            elif not list2:
                node.next = list1
                node = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                node.next = list1
                node = list1
                list1 = list1.next
            else:
                node.next = list2
                node = list2
                list2 = list2.next
        return head

# Beats 65.19% on execution time
# Beats 58.60% on memory usage
