class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0

        sign =1
        result=0
        i=0

        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1


        while i<len(s) and s[i].isdigit():
            result =result*10+int(s[i])
            i+=1
       
        result*=sign

        INT_MIN =-2**31
        INT_MAX=2**31-1

        if result<INT_MIN:
            return INT_MIN
        if result>INT_MAX:
            return INT_MAX


        return result