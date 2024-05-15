class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        left_height = height[left_ptr]
        right_height = height[right_ptr]
        water = 0
        left_peak = left_height
        right_peak = right_height

        while left_ptr < right_ptr:

            if left_height < right_height: 
                left_ptr += 1
                new_left_height = height[left_ptr]
                water_body = left_peak - new_left_height
                left_height = new_left_height
                if left_height > left_peak:
                    left_peak = left_height
            else:
                right_ptr -= 1
                new_right_height = height[right_ptr]
                water_body = right_peak - new_right_height
                right_height = new_right_height
                if right_height > right_peak:
                    right_peak = right_height
            
            print(left_ptr, right_ptr, water_body)
            water += water_body if water_body > 0 else 0
        return water


