# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        c1 = 0
        c2 = 0
        head_copy = head
        while head_copy.next != None:
            c1 += 1
            head_copy = head_copy.next
        head_copy = head
        while head_copy.next != None:
            c2 += 1
            head_copy = head_copy.next
            if c2 == int(c1 / 2) + (c1 & 1):
                return head_copy
        return head
        