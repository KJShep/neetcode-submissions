# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        start = list1
        curr1 = list1
        curr2 = list2
        curr1Prev = None
        curr2Next = None
        while(curr1 is not None and curr2 is not None):
            print(curr1.val,curr2.val)
            if curr2.val < curr1.val:
                if(curr1Prev is not None):
                    curr1Prev.next = curr2
                curr1Prev = curr2
                curr2Next  = curr2.next
                curr2.next = curr1
                curr2 = curr2Next
            else:
                curr1Prev = curr1
                curr1 = curr1.next
        if(curr2 is not None):#curr 1 finished
            curr1Prev.next = curr2
        if list2.val<list1.val:
            start = list2
        return start
        