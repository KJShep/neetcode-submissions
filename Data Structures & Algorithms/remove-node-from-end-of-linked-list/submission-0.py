# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        length = 0
        while(curr is not None):
            length+=1
            curr = curr.next
        curr = head
        for i in range(length - n):
            prev = curr
            curr = curr.next
        if curr is not None and prev is not None:
            prev.next = curr.next
            curr.next = None
        elif prev is not None:
            prev.next = None
        else: #prev is none
            head = head.next
        return head
        