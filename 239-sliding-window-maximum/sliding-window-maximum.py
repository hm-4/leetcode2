class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        It should be called max pooling since it works like 
        max pooling layer in cnns, but is one dimensional.


        [1, 1, 1, 1, 1, 4, 5]  and k=6

        [1, 1, 1, 1, 1, 4], 5 : step1
        1, [1, 1, 1, 1, 4, 5] : step2
        but we don't need to store all first four ones in
        the step 2 because 4 is bigger than that.
        We use the Deque for that called monotonically decresing queue.

        8, 7, 6, 9   and k=2

        deque: 8, 7  (7<=8)
        output: 8

        left pop of deck since window moved to 7, 6
        deque: 7, 6  (6<=7)
        output: 8, 7

        left pop deck, since window moved to 6, 9
        pop from right position, since left most 6 in dequae is less than the 9
        deque: 9

        """
        output = []
        q = collections.deque()
        left_ptr = 0
        for right_ptr in range(len(nums)):
            # after popping all lesser values append the new value
            ## popping from right
            while q and nums[q[-1]] <= nums[right_ptr]:
                q.pop()
            q.append(right_ptr)

            # remove the outgoing element from deque. if that is the 
            # max element now.
            if right_ptr - k >= q[0]:
                q.popleft()
            
            if right_ptr >= k - 1:
                output.append(nums[q[0]])
        return output

            



















        
