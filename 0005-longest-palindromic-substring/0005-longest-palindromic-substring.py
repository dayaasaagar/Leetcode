class Solution:
    def longestPalindrome(self, s: str) -> str:
  
        def expand(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i -=1
                j+=1

            return s[i+1:j]

        res =""

        for i in range(len(s)):

            odd = expand(i,i)

            even = expand(i,i+1)

            res = max(res,odd,even,key=len)

        return res












        