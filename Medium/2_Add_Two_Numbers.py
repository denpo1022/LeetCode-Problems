# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans, root = ListNode(0), ListNode(0)
        root = ans
        while(l1 and l2):
            if(ans.val + l1.val + l2.val >= 10):
                ans.val += l1.val + l2.val
                ans.val %= 10
                l1, l2 = l1.next, l2.next
                ans.next = ListNode(1)
                ans = ans.next
                if(not l1 or not l2):
                    break
            else:
                ans.val += l1.val + l2.val
                l1, l2 = l1.next, l2.next
                if(not l1 and not l2):
                    break
                ans.next = ListNode(0)
                ans = ans.next
                if(not l1 or not l2):
                    break
                
        while(l1 or l2):
            if(l1):
                ans.val += l1.val
                l1 = l1.next
            else:
                ans.val += l2.val
                l2 = l2.next
            if(not l1 and not l2 and ans.val < 10): 
                break
            if(ans.val >= 10):
                ans.val %= 10
                ans.next = ListNode(1)
            else:
                ans.next = ListNode(0)
            ans = ans.next
            
        return root