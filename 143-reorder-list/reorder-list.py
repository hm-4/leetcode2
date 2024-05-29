# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        slow and fast pointer to find the middle of the list.
        
        """
        slow_ptr, fast_ptr = head, head.next
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        second_list = slow_ptr.next
        slow_ptr.next = None # we want to ground the last

        prev = None
        curr = second_list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list1_curr = head
        list2_curr = prev
        # since second list is shoter when the list length even
        # checking only second list curr is enough.
        while list2_curr:
            # detaching fist elements so need two temp variables
            # to store the next pointers
            temp1 = list1_curr.next
            temp2 = list2_curr.next
            list1_curr.next = list2_curr # you wrote head.next = list2_curr
            list2_curr.next = temp1

            list1_curr = temp1
            list2_curr = temp2
