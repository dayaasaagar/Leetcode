import re
class Solution:
    def maxDepth(self, s: str) -> int:

        maxd =0
        curd =0

        for i in range(len(s)):

            if s[i]=='(':
                curd+=1
                maxd= max(maxd,curd)

            elif s[i]==')':
                curd-=1
            
        return maxd








        