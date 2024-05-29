# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for i in range(n):
            if not curr.next:
                # print("hello") 
                # this means we have to remove the first element.
                head = head.next
                return head
            curr = curr.next
        curr = curr.next # to reach the element before

        # run through the list
        position = head
        while curr:
            curr = curr.next
            position = position.next
        
        position.next = position.next.next
        return head

        