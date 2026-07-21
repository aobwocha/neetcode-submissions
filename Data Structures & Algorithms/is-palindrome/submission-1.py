class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0

        while left <= right:
            if not s[right].isalnum():
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                right -= 1
                left += 1
        
        return True
            
        