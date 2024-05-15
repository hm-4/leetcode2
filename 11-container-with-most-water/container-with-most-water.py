class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_left = 0
        p_right = len(height) - 1
        max_area = 0
        difference = (p_right - p_left)
        left_height = height[p_left]
        right_height = height[p_right]

        while difference > 0:
            if left_height < right_height:
                new_area = left_height * difference
                p_left += 1
            else:
                new_area = right_height * difference
                p_right -= 1
            if new_area > max_area:
                max_area = new_area

            difference = (p_right - p_left)
            left_height = height[p_left]
            right_height = height[p_right]
        return max_area



        