class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of the seq by checking left to the number
            if (n-1) not in numSet:
                # start of a seq
                length = 0
                # check all the rigght numbers
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest