class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        # print(nums, not nums)
        if not nums:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # target on left.
            return self.search(nums[:mid], target)
        else:
            # target on right
            got = self.search(nums[mid+1:], target)
            return (mid + 1 + got) if got >= 0 else -1

        
        