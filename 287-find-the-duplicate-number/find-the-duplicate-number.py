class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast start at begining index
        slow, fast = 0, 0
        while True:
            # break when slow and fast are equal
            slow = nums[slow] # one step at a time
            fast = nums[nums[fast]] # two steps at a time
            if slow == fast:
                break
        # start new slow pointer at the begining index
        slow2 = 0
        while True:
            # return when slow and slow2 meets
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        