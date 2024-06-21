class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s)-1
        while left_ptr < right_ptr:
            

            while left_ptr < right_ptr and not self.alphaNum(s[left_ptr]):
                left_ptr += 1
            while left_ptr < right_ptr and not self.alphaNum(s[right_ptr]):
                right_ptr -= 1

            if s[left_ptr].lower() != s[right_ptr].lower():
                return False
            left_ptr += 1
            right_ptr -= 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
