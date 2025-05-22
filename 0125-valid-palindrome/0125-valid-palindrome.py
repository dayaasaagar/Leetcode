import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = re.sub(r'[^A-Za-z0-9]+', '', s).lower()

        return newstring==newstring[::-1]
        