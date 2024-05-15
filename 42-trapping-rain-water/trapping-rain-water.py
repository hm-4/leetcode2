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
                left_height = height[left_ptr]
                water_body = left_peak - left_height
                left_peak = max(left_peak, left_height)
            else:
                right_ptr -= 1
                right_height = height[right_ptr]
                water_body = right_peak - right_height
                right_peak = max(right_peak, right_height)
            
            water += water_body if water_body > 0 else 0
        return water


