class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()
        
        while n!=1 and n not in nset:
            nset.add(n)
            total =0
            while n>0:
                rem= n%10
                total+=rem*rem
                n=n//10
            n=total
        
        return n==1

        