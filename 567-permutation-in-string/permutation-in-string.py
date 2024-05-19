class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        we will have exactly |s2| - |s1| + 1 windows, 
        using a window size of |s1|. Each such window 
        in s2 can be compared with s1, which takes 26
        operations, hash map.

        Better solution:
        s1: abc
           |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|
           |1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|

        s2: baxyzabc
        --------------------------------------------------------
        window1: "bax"yzabc
           |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|
        w1:|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|
        
        matches: 26 - 2 matches = 24 matches

        --------------------------------------------------------
        shift window right!!
        window2: b"axy"zabc
           |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|
        w1:|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|
        w2:|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|0|

        matches: 24 previous matches, one match for 'b' is gone,
        and one mis match for new char 'y'. therefore 24 - 1 -1.
        22 matches.


        when matches are 26. we can stop the code.

        The edge case:
        -------------
        if len of s1 is greater than s2 then we cannot find the
        permutation, so return False.
        """
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len: return False

        s1_count = {chr(i):0 for i in range(ord('a'), ord('a') + 26)}
        s2_count = {chr(i):0 for i in range(ord('a'), ord('a') + 26)}

        for i in range(s1_len):

            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        #print(s1_count)
        matches = 0
        for key in s1_count:
            if s1_count[key] == s2_count[key]:
                matches += 1
        #print(matches)

        for right in range(s1_len, s2_len):
            if matches == 26: return True

            new_char = s2[right]
            s2_count[new_char] += 1
            if s2_count[new_char] == s1_count[new_char]:
                matches += 1
            elif s2_count[new_char] - 1 == s1_count[new_char]:
                # this means previous count match, 
                # and current mismatched so matches should reduce.
                matches -= 1
            
            out_char = s2[right - s1_len]
            s2_count[out_char] -= 1
            if s2_count[out_char] == s1_count[out_char]:
                matches += 1
            elif s2_count[out_char] + 1 == s1_count[out_char]:
                # this means previous count match, 
                # and current mismatched so matches should reduce.
                matches -= 1
        return matches == 26





        