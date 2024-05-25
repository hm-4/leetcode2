class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1


        if nums[left_ptr] < nums[right_ptr]: 
            return nums[left_ptr]

        while left_ptr < right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2
            # print(left_ptr, right_ptr, mid_ptr, left_val, right_val, mid_val)
            if nums[mid_ptr] >= nums[left_ptr] and nums[left_ptr] > nums[right_ptr]:
                """
                it should be greater than or equal since for a case like [2, 1]
                and nums[left_ptr] > nums[right_ptr]: statement should be there
                when the pointer are on the right side of the array which is in 
                increasing order, we have to distinguish that from the left side
                case where we the array may not be in increasing order.
                """
                left_ptr = mid_ptr + 1
                # mid_ptr is always in the list since
                # since interdivision will result in this phenomenon.
                # (1+2) // 2 = 1 and 1+1 = 2, two is already valid index.

            else:
                right_ptr = mid_ptr  
                # should not be right_ptr=mid_ptr-1 because 
                # the the mid_val can be the minimum val 

            
        return nums[left_ptr]
        