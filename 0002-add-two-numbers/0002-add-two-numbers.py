# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        node1 = []
        while node is not None:
            node1.append(node.val)
            node = node.next
        node1[:] = node1[::-1]
        strs = list(map(str, node1))
        str1 = "".join(strs)
        num1 = int(str1)
        print(str1)

        node = l2
        node2 = []
        while node is not None:
            node2.append(node.val)
            node = node.next
        node2[:] = node2[::-1]
        string = list(map(str, node2))
        str2 = "".join(string)
        num2 = int(str2)
        print(str2)

        result = num1 + num2
        digits = list(map(int, str(result)))
        digits[:] = digits[::-1]
        head = ListNode(digits[0])
        node = head
        for i in range(1,len(digits)):
            node.next = ListNode(digits[i])
            node = node.next
        return head

            
            



            


        
        