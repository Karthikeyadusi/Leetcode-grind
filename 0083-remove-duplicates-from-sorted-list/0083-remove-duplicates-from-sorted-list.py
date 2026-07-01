# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = head
        while current:
          if current.next:
            while current.val == current.next.val:
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
                    return head
          current = current.next
        return head
        
        