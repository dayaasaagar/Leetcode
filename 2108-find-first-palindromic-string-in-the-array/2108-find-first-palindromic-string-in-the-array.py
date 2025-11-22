class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def palindrom(word):
            if word == word[::-1]:
                return True 
            else:
                return False
        for i in words:
            if palindrom(i):
                return i
        return ""
        