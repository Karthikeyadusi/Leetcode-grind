# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        last = dummy
        current1, current2 = list1, list2
        while current1 and current2:
            if current1.val <= current2.val:
                last.next = current1
                last = current1
                current1 = current1.next
            elif current2.val < current1.val:
                last.next = current2
                last = current2
                current2 = current2.next
        if current1 is None or current2 is None:
            if current1 is None:
                last.next = current2
            else:
                last.next = current1
        return dummy.next
        