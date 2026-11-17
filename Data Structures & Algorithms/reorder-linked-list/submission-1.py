# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #2->4->6->[8->10]
        #        [10,8]
        #Grab the second half of linked list, reverse it
        #zip the 2 lists

        #get length
        length = 0
        curr = head
        while(curr != None):
            length += 1
            curr = curr.next
        if length == 1:
            return
        middleIndex = math.ceil(length/2)
        reverseStart = head
        prev = None
        for i in range(middleIndex):
            prev = reverseStart
            reverseStart = reverseStart.next
        prev.next= None
        #reverse second half
        curr = reverseStart
        prev = None
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        reverseCurr = prev
        #zip
        curr = head
        while(curr != None):
            temp1 = curr.next
            curr.next = reverseCurr
            if reverseCurr != None:
                temp2 = reverseCurr.next
                reverseCurr.next = temp1
            curr = temp1
            reverseCurr = temp2




        