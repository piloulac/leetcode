# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        s = t = ListNode()
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                c = l1
                l1 = l1.next
            else:
                c = l2
                l2 = l2.next
            
            t.next = c 
            t = t.next
        
        t.next = l1 or l2
        
        return s.next