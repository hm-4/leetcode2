class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        row_exist = False # initally no row exist s.t. target is in that row.
        target_row = 0
        while top <= bottom:

            mid_row = (top + bottom) // 2
            target_row = mid_row
            if matrix[mid_row][-1] < target: 
                # if last in the row is lesser than target
                top = mid_row + 1
            elif matrix[mid_row][0] > target:
                # if first element is bigger than target
                bottom = mid_row - 1
            else:
                # target should be in this row 
                # target_row = mid_row # target row should be updated if this is 
                row_exist = True
                break # didn't consider writing break, if non of the conditions are 
                # true we want to break the loop
            # print(row_exist)
        if not row_exist:
            return False
        else:
            left = 0
            right = cols - 1
            while left <= right:
                mid_col = (left+right) // 2
                if matrix[target_row][mid_col] == target:
                    return True
                elif matrix[target_row][mid_col] > target:
                    right = mid_col - 1
                else:
                    left = mid_col + 1 # spelling mistakes causing time limit exceeding.

            return False



    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows = len(matrix)
        # cols = len(matrix[0])
        # top = 0
        # bottom = rows - 1

        # while top < bottom:
        #     print(top, bottom)
        #     mid_row = (top + bottom) // 2
        #     if matrix[mid_row][0] > target:
        #         bottom = mid_row - 1
        #     else: ### **** don't know how to find the pointer eventually ****
        #         top = mid_row 

        # left = 0
        # right = cols - 1
        # while left <= right:
        #     mid_col = (left+right)//2
        #     if matrix[top][mid_col] == target:
        #         return True
        #     elif matrix[top][mid_col] > target:
        #         right = mid_col - 1
        #     else:
        #         lefft = left + 1
        # return False



        