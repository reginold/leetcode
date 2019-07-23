# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        result = root
        carry = 0
        
        while l1 or l2 or carry == 1:
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            value += carry
            root.next = ListNode(value%10)
            carry = int(value / 10)
            root = root.next
        return result.next