# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None
        slow, fast = head,head
        previous = slow
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        previous.next = slow.next
        return head

        
        