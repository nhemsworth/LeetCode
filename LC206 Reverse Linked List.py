from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        prev_node = head
        node = head.next
        head.next = None

        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return prev_node


sol = Solution()

A = ListNode(val=2)
B = ListNode(val=1, next=A)
C = ListNode(val=0, next=B)

node = C

while node:
    print(node.val)
    node = node.next

node = C

head_r = sol.reverseList(node)
node = head_r

while node:
    print(node.val)
    node = node.next

# Beats 97.67% on execution time
# Beats 76.55% on memory usage
