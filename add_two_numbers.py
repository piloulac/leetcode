# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNumber(self, l: ListNode, puissance: int) -> int: 
        if l.next == None:
            return l.val*puissance
        else:
            return l.val*puissance + self.getNumber(l.next, puissance*10)
    
    def createListNodeFromNum(self, value: int) -> ListNode:
        if value/10 < 1:
            return ListNode(value)
        else:
            return ListNode(value%10, self.createListNodeFromNum(value//10))
            
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        my_sum = self.getNumber(l1,1) + self.getNumber(l2,1)
        return self.createListNodeFromNum(my_sum)
        