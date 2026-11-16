# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr0 = head
        while curr0:
            length += 1
            curr0 = curr0.next

        n = length - n

        if n == 0:                   
            return head.next          

        curr = head
        for i in range(n - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head


            

        
        