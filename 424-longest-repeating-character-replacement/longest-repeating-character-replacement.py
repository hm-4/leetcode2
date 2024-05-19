class Solution:
    def characterReplacement2(self, s: str, k: int) -> int:
        count={}#stores frequency of each letter in that window
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)

            while(r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window style:
        valid_window: window of size w and of which we have atleast w-k are 
        most frequent charecters. If the above condition is satify then that 
        window size w is valid. 
        The condition can be rewritten as: 
                 w-m <= k, 
                 w: window size, m: most freqent charecter count in the window w.

        so for every silding window, we caluclate m among 26 charecters, this is O(26)
        we want to reduce that too.


        The window right_ptr goes up every loop. The left ptr moves up when the 
        condition is not met. when right pointer up we increase the count of the 
        new charecter by one. when the left pointer moves up then we decrease the 
        count of outgoing charecter(from window) by one. the maxfrequency is the 
        variable that counts max possible frequency of a charecter that we have seen 
        till now in a window. and result variable stores the window maximum window 
        we have seen till now. 
        
        """
        count={}#stores frequency of each letter in that window
        res=0
        l=0
        maxf=0
        for r in range(len(s)):
            count[s[r]]=1 +count.get(s[r],0)
            maxf=max(maxf,count[s[r]])#saves time

            while(r-l+1)-maxf > k:#saves time
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res