# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # both tortoise and hare starts at same point
        while fast and fast.next:
            # till we reach the end
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False