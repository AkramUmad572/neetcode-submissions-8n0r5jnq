# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None and list2:
            return list2
        if list1 and list2 == None:
            return list1
        p1,p2 = list1, list2
        dummy = ListNode()
        tail = dummy

        while p1 and p2:
            if p1.val >= p2.val:
                tail.next = p2
                p2 = p2.next
            else:
                tail.next = p1
                p1 = p1.next
            tail = tail.next
        
        if p1 != None:
            tail.next = p1
        if p2 != None:
            tail.next = p2
        return dummy.next
