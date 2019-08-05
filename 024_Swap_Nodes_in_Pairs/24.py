# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 利用迭代的思想，先设置一个空，然后不断的叠加
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            p1 = curr.next
            p2 = curr.next.next

            # 交换两个pointer
            p1.next = p2.next
            p2.next = p1
            curr.next = p2

            # 更新到下一个节点
            curr = curr.next.next
        return dummy.next


