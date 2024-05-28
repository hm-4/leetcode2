# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        last = ListNode()
        head = last
        while list1 and list2:
            # print(list1.val, list2.val)
            if list1.val >= list2.val:
                last.next = list2
                list2 = list2.next

            else:
                last.next = list1
                list1 = list1.next

            last = last.next
            last.next = None
            # print(last)
        if not list1:
            last.next = list2
        else:
            last.next = list1
        
        return head.next
        


        