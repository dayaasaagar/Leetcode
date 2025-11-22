class Solution:
    def countDigits(self, num: int) -> int:
        old =num
        count=0
        while num>0:
            digit=num%10
            if digit!=0 and old%digit==0:
                count+=1
            num //=10
        return count
        











        