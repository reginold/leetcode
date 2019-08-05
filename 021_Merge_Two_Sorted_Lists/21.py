class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


def initList(array):
    root = ListNode(array[0])
    result = root
    for index, value in enumerate(array):
        if index > 0:
            root.next = ListNode(value)
            root = root.next
    return result


def printList(linkList):
    if linkList:
        print("[", end="")
        while linkList.next:
            print(linkList.val, end=",")
            linkList = linkList.next
        print(linkList.val, end="]\n")
    else:
        print("[]")


if __name__ == "__main__":
    l1 = initList([1, 2, 4])
    l2 = initList([1, 3, 4])
    solution = Solution()
    printList(solution.mergeTwoLists(l1, l2)) == [1,1,2,3,4,4]
    print("Well Done, Go Summit")
