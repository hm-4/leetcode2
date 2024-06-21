# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head) ## dummy node will help you to get the kth node as head
        ## else it would make your life difficult.
        last = dummy
        curr = head
        count = 0
        while curr:
            count += 1
            prev = curr
            curr = curr.next
            if count == k:
                
                new_head = self.reverse(head, curr)
                last.next = new_head
                
                last = head
                head = curr
                count = 0
        return dummy.next




    def reverse(self, curr_group_head, next_group_head):
        prev = next_group_head
        head = curr_group_head
        while curr_group_head is not next_group_head:
            save_next_ptr = curr_group_head.next
            curr_group_head.next = prev

            prev = curr_group_head
            curr_group_head = save_next_ptr
        return prev
