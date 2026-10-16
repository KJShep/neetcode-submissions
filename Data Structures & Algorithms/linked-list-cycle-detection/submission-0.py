# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        curr = head
        while(curr is not None):
            visited[curr] = visited.get(curr,0) + 1
            if visited[curr] >1:
                return True
            curr = curr.next
        return False
        