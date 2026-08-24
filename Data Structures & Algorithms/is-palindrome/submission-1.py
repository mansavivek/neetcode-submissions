class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(''.join( c for c in s if c.isalnum()).lower())
        return s == s[::-1]

        