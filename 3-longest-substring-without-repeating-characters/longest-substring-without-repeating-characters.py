class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        |    |  |             |       |
        |  | |  | | |||       |  |  | |
        | || | || |    |||   ||  |  | |
        ||||||||||||      ||||||||||||||
        1 2

        """
        n = len(s)
        left = 0 
        charDict = {}
        maxLength = 0

        for right in range(n):
            if s[right] not in charDict or charDict[s[right]] < left:
                """ CharDict[s[right]] < left: as the dictionary is not cleared,
                the previous string values must be there in the dictionary, so we
                check if the index for the new char is less than the leftptr index or not
                if it is less than than leftptr it means it is from the provious strings.
                In this case we treat the condition same as the char not presenting in the 
                dictionary.

                s[right] not in charDict: if the char is not in the dictionary we create a key
                of that charecter and value is the index of the char i.e rightptr.

                update the maxlength.
                """
                charDict[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
                # print(f"left/right: {left}{right}")
            else:
                """ if the newchar is present in the dictionary we change leftptr to the 
                next index of the already presented char's index.
                and update the char value to new index i.e righptr.
                """
                left = charDict[s[right]] + 1
                charDict[s[right]] = right
        # indentation you should not do wrong. afterloop we have to return the 
        # maxLength, not in between. that is why it is giving answe as 1 every time
        # since it is breaking and returning after one loop.
        return maxLength
