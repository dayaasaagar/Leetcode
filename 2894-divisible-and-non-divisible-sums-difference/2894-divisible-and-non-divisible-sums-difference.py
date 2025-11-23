class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        msum =0
        nmsum=0

        for i in range(1,n+1):
            if i%m==0:
                msum += i
            else:
                nmsum +=i
        return nmsum-msum

        