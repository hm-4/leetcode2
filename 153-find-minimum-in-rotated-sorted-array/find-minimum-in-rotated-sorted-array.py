class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1
        left_val = nums[left_ptr]
        right_val = nums[right_ptr]

        if left_val < right_val: 
            return left_val

        while left_ptr < right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2
            mid_val = nums[mid_ptr]
            print(left_ptr, right_ptr, mid_ptr, left_val, right_val, mid_val)
            if mid_val >= left_val and left_val > right_val:
                left_ptr = mid_ptr + 1
                # mid_ptr is always in the list since
                # since interdivision will result in this phenomenon.
                # (1+2) // 2 = 1 and 1+1 = 2, two is already valid index.
                left_val = nums[left_ptr]
            else:
                right_ptr = mid_ptr  
                # should not be right_ptr=mid_ptr-1 because 
                # the the mid_val can be the minimum val 
                right_val = nums[right_ptr]
            
        return left_val
        