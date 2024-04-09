class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        original_x = x
        num_reversed = 0
        while x>0:
            last_digit = x%10
            num_reversed = num_reversed * 10 + last_digit
            x//=10
        return num_reversed == original_x
