class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        def _isPal(s: str) -> bool:
            if len(s) <= 1:
                return True
            else:
                return s[0]==s[-1] and _isPal(s[1:-1])
        
        return _isPal(s)