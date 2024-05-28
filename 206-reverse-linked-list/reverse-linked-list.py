# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##### **** don't need two heads ****
        # if not head:
        #     return head
        # elif not head.next:
        #     return head
        # else:
        #     r_ptr = head.next.next
        #     m_ptr = head.next
        #     head.next = None
        #     while r_ptr:
        #         m_ptr.next = head
        #         head = m_ptr
        #         m_ptr = r_ptr
        #         r_ptr = m_ptr.next
            
        #     m_ptr.next = head
        #     head = m_ptr
        #     return head


        ####  ** Simpler solution **
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        #### ** Recursive solution **

        # if not head:
        #     return None
        # new_head = None
        # if head.next:
        #     new_head = self.reverseList(head.next)
        #     head.next.next = head
        # else:
        #     new_head = head
        # head.next = None
        # return new_head
        



