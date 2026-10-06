# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        small, fast = head, head 

        while fast and fast.next:
            small = small.next
            fast = fast.next.next
            if small == fast:
                return True
        return False